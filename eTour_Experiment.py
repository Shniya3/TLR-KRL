import operator
import os
import re

import LogicalReasoning
import openTxt
import numpy as np
import sklearn
import random
import Result
import Phase3Classifier
import Phase2
import csv
import math
import TripleClassfication
import InformationRetrivalMethod
import Component

def loadData_tranE(str):
    fr = open(str, encoding="utf-8")
    sArr = [line.strip().split("\t") for line in fr.readlines()]
    datArr = [[float(s) for s in line[1][1:-1].split(", ")] for line in sArr]
    nameArr = [line[0] for line in sArr]
    return datArr, nameArr


def loadData_KB2E(str):
    fr = open(str, encoding="utf-8")
    sArr = [line.strip().split("\t") for line in fr.readlines()]
    datArr = [[float(s) for s in line] for line in sArr]
    return datArr


def loadData_DKRL(dir1, dir2):
    with open(dir1, encoding="utf-8") as file:
        lines = file.readlines()
    with open(dir2, encoding="utf-8") as file:
        ids = file.readlines()
    vec_dict = {}
    for index, (line, id) in enumerate(zip(lines, ids)):
        temp_list = []
        for i in line.split("\t")[0:-1]:
            temp_list.append(float(i))
        vec_dict[id.split("\t")[0]] = temp_list
    return vec_dict

def generateClassiferData(train,test,oracleList,cnn2vec,stru2vec,FLAG,rate):
    uc_list = []
    cc_list = []
    uc2code_oracle_all = []
    uc2code_oracle_train = []
    uc2code_oracle_test = []
    uc2code_F_triple = []
    for triple in train + test:
        if triple[2] == "oracle_link":
            if triple[0] not in uc_list:
                uc_list.append(triple[0])
            if triple[1] not in cc_list:
                cc_list.append(triple[1])

    for uc in uc_list:
        for i in cnn2vec[uc]:
            if math.isnan(float(i)):
                uc_list.pop(uc_list.index(uc))
                break

    for cc in cc_list:
        for i in cnn2vec[cc]:
            if math.isnan(float(i)):
                cc_list.pop(cc_list.index(cc))
                break

    for triple in train:
        if triple[2] == "oracle_link" and triple[1] in cc_list:
            uc2code_oracle_train.append(triple)
            uc2code_oracle_all.append(triple)
    for triple in test:
        if triple[2] == "oracle_link" and triple[1] in cc_list:
            uc2code_oracle_test.append(triple)
            uc2code_oracle_all.append(triple)

    for uc in uc_list:
        for cc in cc_list:
            if (uc, cc, "oracle_link") not in uc2code_oracle_all:
                uc2code_F_triple.append((uc, cc, "oracle_link"))

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    x_test_triple = []
    ###正样本训练集
    print(cnn2vec["UC2"])
    for triple in uc2code_oracle_train:
        if triple[0] not in uc_list:
            continue
        if triple[1] not in cc_list:
            continue
        if FLAG:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))
        if np.isnan(vector).any():
            print(triple)
        x_train.append(vector)
        y_train.append(1)
    for triple in uc2code_oracle_test:
        if triple[0] not in uc_list:
            continue
        if triple[1] not in cc_list:
            continue
        if FLAG:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))

        x_test.append(vector)
        x_test_triple.append(triple)
        y_test.append(1)
    for triple in uc2code_F_triple:
        if triple[0] not in uc_list:
            continue
        if triple[1] not in cc_list:
            continue
        if FLAG:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))
        if np.isnan(vector).any():
            print(triple)
        if random.random() < (rate):
            x_train.append(vector)
            y_train.append(0)
        else:
            x_test.append(vector)
            x_test_triple.append(triple)
            y_test.append(0)
    return x_train,y_train,x_test,y_test,x_test_triple

    ###要不要进行10折？
    ###

def vector_sub(vector1,vector2):
    res = []
    for v1,v2 in zip(vector1,vector2):
        res.append(v1-v2)
    return res

def orgnanizeDataFormat(DkrlTrain,TrainN,DkrlTest,ClassiferTestTriples,cnn2vec,stru2vec,FLAG):
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    x_test_triple = []
    ###正样本训练集
    print(cnn2vec["UC2"])
    for triple in DkrlTrain:
        if triple[2] != "oracle_link":
            continue
        # if triple[0] not in uc_list:
        #     continue
        # if triple[1] not in cc_list:
        #     continue
        if FLAG ==2 :
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        elif FLAG ==1 :
            temp = vector_sub(cnn2vec[triple[0]],cnn2vec[triple[1]])+vector_sub(stru2vec[triple[0]],stru2vec[triple[1]])
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))
        if np.isnan(vector).any():
            print(triple)
        x_train.append(vector)
        y_train.append(1)

    for triple in TrainN:
        # if triple[0] not in uc_list:
        #     continue
        # if triple[1] not in cc_list:
        #     continue
        if FLAG ==2 :
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        elif FLAG ==1 :
            temp = vector_sub(cnn2vec[triple[0]],cnn2vec[triple[1]])+vector_sub(stru2vec[triple[0]],stru2vec[triple[1]])
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))
        x_train.append(vector)
        # x_test_triple.append(triple)
        y_train.append(0)
    for triple in ClassiferTestTriples:
        # if triple[0] not in uc_list:
        #     continue
        # if triple[1] not in cc_list:
        #     continue
        if FLAG ==2 :
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]+stru2vec[triple[0]]+stru2vec[triple[1]]
        elif FLAG ==1 :
            temp = vector_sub(cnn2vec[triple[0]],cnn2vec[triple[1]])+vector_sub(stru2vec[triple[0]],stru2vec[triple[1]])
        else:
            temp = cnn2vec[triple[0]] + cnn2vec[triple[1]]
        vector = []
        for w in temp:
            vector.append(float(w))
        if np.isnan(vector).any():
            print(triple)
        if triple in DkrlTest:
            x_test.append(vector)
            x_test_triple.append(triple)
            y_test.append(1)
        else:
            x_test.append(vector)
            x_test_triple.append(triple)
            y_test.append(0)
    return x_train,y_train,x_test,y_test,x_test_triple

if __name__ == '__main__':
    cnn2vec = loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/cnn_vec_out.txt", "./data/eTour/train_data/entity2id.txt")
    rel2vec = loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/relation2vec.bern", "./data/eTour/train_data/relation2id.txt")
    stru2vec = loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/entity2vec.bern", "./data/eTour/train_data/entity2id.txt")
    # test_num, test = openTxt.openTrain("./data/eTour/train_data/testZ.txt")
    # train_num, train = openTxt.openTrain("./data/eTour/train_data/trainZ.txt")
    # oracle_num,oracleList = openTxt.openOracle("./data/eTour/oracle/oracle line.txt")
    dkrl_train_num,dkrl_train = openTxt.openTrain("./data/eTour/train_data/DKRL_trainZ.txt")
    dkrl_test_num,dkrl_test = openTxt.openTrain("./data/eTour/train_data/DKRL_testZ.txt")
    trainZ_N_num,trainZ_N = openTxt.openTrain("./data/eTour/train_data/trainZ_N.txt")
    ClassiferTestTriples_Num,ClassiferTestTriples = openTxt.openTrain("./data/eTour/train_data/Classifer_test_Z.txt")

    x_train, y_train, x_test, y_test,x_test_triple = orgnanizeDataFormat(dkrl_train,trainZ_N,dkrl_test,ClassiferTestTriples,cnn2vec,stru2vec,1)

    y_predict = Phase3Classifier.train(x_train, y_train, x_test, y_test, 1)
    precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)

    y_predict = Phase3Classifier.train(x_train, y_train, x_test, y_test, 2)
    precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    y_predict = Phase3Classifier.train(x_train, y_train, x_test, y_test, 4)
    precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    y_predict = Phase3Classifier.train(x_train, y_train, x_test, y_test, 6)
    precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    # y_predict = InformationRetrivalMethod.IR_Rank(cnn2vec,stru2vec,100,0.5,"cosine",dkrl_train,trainZ_N,ClassiferTestTriples)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    ### x_train, y_train, x_test, y_test,x_test_triple = generateClassiferData(train,test,oracleList,cnn2vec,stru2vec,1,(4/7))
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_multi)
    # y_predict = Phase1.train(x_train, y_train, x_test, y_test,2)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    ## 这是Improve的svm参数##
    # model = sklearn.svm.SVC(C=0.017538469504833957, break_ties=False, cache_size=200,
    #                                  class_weight='balanced', coef0=0.0, decision_function_shape='ovr', degree=3,
    #                                  gamma=2.8284271247461903, kernel='poly', max_iter=-1, probability=True,
    #                                  random_state=None, shrinking=True, tol=0.001, verbose=False)

    # model = sklearn.svm.SVC(C=32768.0, break_ties=False, cache_size=200, class_weight='balanced',
    #     coef0=0.0, decision_function_shape='ovr', degree=4,
    #     gamma=0.04419417382415922, kernel='poly', max_iter=-1, probability=False,
    #     random_state=None, shrinking=True, tol=0.001, verbose=False)
    # model.fit(x_train, y_train)
    # y_score = model.decision_function(x_test)
    # min = 0
    # max = 0
    # for score in y_score:
    #     if min > score:
    #         min = score
    #     if max <score:
    #         max = score
    # thresholds = np.linspace(min,max,100)
    # recordList = []
    # y_predict_init = [np.int32(0) for i in range(0,len(x_test))]
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict_init,cnn2vec,stru2vec,rel2vec,0.85)
    # print("only triple classification")
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    # #
    # rates = np.linspace(0.8,1,20)
    # rates = [0.01*i for i in range(80,101)]
    # print(rates)
    # y_predict = Component.scoreToPredict(0,y_score)
    # print("only svm")
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    # for threshold in thresholds:
    #     for rate in rates:
    #         y_predict = Component.scoreToPredict(threshold,y_score)
    #         y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,rate,False)
    #         precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    #         if [precissio, recall, acc, f1] not in recordList:
    #             recordList.append([precissio, recall, acc, f1])
    #
    # recordList.sort(key=Component.takeSecond)
    # with open("./data/eTour/experimentResult.txt","w",encoding="utf-8") as file:
    #     for result in recordList:
    #         file.write(str(result[0])+"\t"+str(result[1])+"\t"+str(result[2])+"\t"+str(result[3])+"\n")



    ###precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
    # ###三元组分类
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,0.8)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    #
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,0.85)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    #
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,0.95)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    #
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(dkrl_train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,1)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)


    # ###规则1推理
    # y_predict_LR_1 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict,1,0,0,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_1)
    # ###规则2推理
    # y_predict_LR_2 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict_cnn,0,1,0,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_2)
    # ###规则3推理
    # y_predict_LR_3 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict,0,0,1,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_3)
    # ###规则4推理
    # y_predict_LR_4 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict,0,0,0,1)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_4)
    # ###三元组加规则1
    # print("三元组加规则1")
    # y_predict_LR_T1 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict_cnn,1,0,0,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_T1)
    # ###三元组加规则2
    # print("三元组加规则2")
    # y_predict_LR_T2 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict_cnn,0,1,0,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_T2)
    # ###规则1+规则2
    # print("规则1加规则2")
    # y_predict_LR_12 = LogicalReasoning.LogicalReasoning(dkrl_train,x_test_triple,y_predict_LR_1,0,1,0,0)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_LR_12)
