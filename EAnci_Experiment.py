import os
import re
import openTxt
import numpy as np
import sklearn
import random
import Result
import Phase3Classifier
import Phase2
import csv
import math
# import SameInheritClass_Recovery
import TripleClassfication

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

def generateClassiferData(train,test,cnn2vec,stru2vec,FLAG,rate):
    uc_list = []
    cc_list = []
    uc2code_oracle_all = []
    uc2code_oracle_train = []
    uc2code_oracle_test = []
    uc2code_F_triple = []
    for triple in train:
        if triple[2] == "oracle_link":
            if triple[0] not in uc_list:
                uc_list.append(triple[0])
            if triple[1] not in cc_list:
                cc_list.append(triple[1])
    for triple in test:
        if triple[2] == "oracle_link":
            if triple[0] not in uc_list:
                uc_list.append(triple[0])
            if triple[1] not in cc_list:
                cc_list.append(triple[1])

    uc_list.append("EA35")
    uc_list.append("EA39")
    uc_list.append("EA40")
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

    for triple in train + test:
        if triple[2] == "oracle_link" and triple[1] in cc_list:
            uc2code_oracle_all.append(triple)

    for triple in train:
        if triple[2] == "oracle_link" and triple[1] in cc_list:
            uc2code_oracle_train.append(triple)

    for triple in test:
        if triple[2] == "oracle_link" and triple[1] in cc_list:
            uc2code_oracle_test.append(triple)

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

if __name__ == '__main__':

    # cnn2vec = loadData_DKRL("./data/500nepoches/res_3_4_500/cnn_vec_out.txt", "./data/train_data/entity2id.txt")
    # rel2vec = loadData_DKRL("./data/500nepoches/res_3_4_500/relation2vec.bern", "./data/train_data/relation2id.txt")
    # stru2vec = loadData_DKRL("./data/500nepoches/res_3_4_500/entity2vec.bern", "./data/train_data/entity2id.txt")
    # test_num, test = openTxt.openTrain("./data/train_data/test_3_4.txt")
    # train_num, train = openTxt.openTrain("./data/train_data/train_3_4.txt")

    # cnn2vec = loadData_DKRL("./data/500nepoches/res_4_7_500/cnn_vec_out.txt", "./data/train_data/entity2id.txt")
    # rel2vec = loadData_DKRL("./data/500nepoches/res_4_7_500/relation2vec.bern", "./data/train_data/relation2id.txt")
    # stru2vec = loadData_DKRL("./data/500nepoches/res_4_7_500/entity2vec.bern", "./data/train_data/entity2id.txt")
    # test_num, test = openTxt.openTrain("./data/train_data/test_4_7.txt")
    # train_num, train = openTxt.openTrain("./data/train_data/train_4_7.txt")

    # cnn2vec = loadData_DKRL("./data/1000nepoches/res_3_4_1000/cnn_vec_out.txt", "./data/train_data/entity2id.txt")
    # rel2vec = loadData_DKRL("./data/1000nepoches/res_3_4_1000/relation2vec.bern", "./data/train_data/relation2id.txt")
    # stru2vec = loadData_DKRL("./data/1000nepoches/res_3_4_1000/entity2vec.bern", "./data/train_data/entity2id.txt")
    # test_num, test = openTxt.openTrain("./data/train_data/test_3_4.txt")
    # train_num, train = openTxt.openTrain("./data/train_data/train_3_4.txt")

    cnn2vec = loadData_DKRL("./data/EAnci/1000nepoches/res_4_7_1000/cnn_vec_out.txt", "./data/train_data/entity2id.txt")
    rel2vec = loadData_DKRL("./data/EAnci/1000nepoches/res_4_7_1000/relation2vec.bern", "./data/train_data/relation2id.txt")
    stru2vec = loadData_DKRL("./data/EAnci/1000nepoches/res_4_7_1000/entity2vec.bern", "./data/train_data/entity2id.txt")
    test_num, test = openTxt.openTrain("./data/train_data/test_4_7.txt")
    train_num, train = openTxt.openTrain("./data/train_data/train_4_7.txt")

    ###new_y_predict = SameInheritClass_Recovery.SameInheritClassRecovery(x_test_triple,y_predict,train)
    ###precissio, recall, acc, f1 = Result.get_result(y_test, new_y_predict)
    ###三元组分类
    # print("rate = {}".format(0.85))
    # y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,0.85)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
    # precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_multi)
    sum1,sum2,sum3,sum4 = 0,0,0,0
    sum5,sum6,sum7,sum8 = 0,0,0,0
    for i in range(0,10):
        x_train, y_train, x_test, y_test,x_test_triple = generateClassiferData(train,test,cnn2vec,stru2vec,1,(4/7))
        y_predict = Phase3Classifier.train(x_train, y_train, x_test, y_test, 1)
        precissio, recall, acc, f1 = Result.get_result(y_test, y_predict)
        print(precissio)
        print(type(precissio))
        sum1+=float(precissio)
        sum2+=float(recall)
        sum3+=float(acc)
        sum4+=float(f1)
        y_predict_cnn,y_predict_multi = TripleClassfication.TripleClassfication(train,x_test_triple,y_predict,cnn2vec,stru2vec,rel2vec,0.85)
        precissio, recall, acc, f1 = Result.get_result(y_test, y_predict_cnn)
        sum5+=float(precissio)
        sum6+=float(recall)
        sum7+=float(acc)
        sum8+=float(f1)

    print("precission:{}".format(sum1/10))
    print("recall:{}".format(sum2/10))
    print("acc:{}".format(sum3/10))
    print("f1:{}".format(sum4/10))
    print("precission:{}".format(sum5/10))
    print("recall:{}".format(sum6/10))
    print("acc:{}".format(sum7/10))
    print("f1:{}".format(sum8/10))