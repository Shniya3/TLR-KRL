import eTour_Experiment
import openTxt
from time import time
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)

if __name__ == '__main__':
    cnn2vec = eTour_Experiment.loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/cnn_vec_out.txt", "./data/eTour/train_data/entity2id.txt")
    rel2vec = eTour_Experiment.loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/relation2vec.bern", "./data/eTour/train_data/relation2id.txt")
    stru2vec = eTour_Experiment.loadData_DKRL("./data/eTour/dkrl_result/res_eTour_1200_100_H_M_Improve/entity2vec.bern", "./data/eTour/train_data/entity2id.txt")
    # test_num, test = openTxt.openTrain("./data/eTour/train_data/testZ.txt")
    # train_num, train = openTxt.openTrain("./data/eTour/train_data/trainZ.txt")
    # oracle_num,oracleList = openTxt.openOracle("./data/eTour/oracle/oracle line.txt")
    dkrl_train_num,dkrl_train = openTxt.openTrain("./data/eTour/train_data/DKRL_trainZ.txt")
    dkrl_test_num,dkrl_test = openTxt.openTrain("./data/eTour/train_data/DKRL_testZ.txt")
    trainZ_N_num,trainZ_N = openTxt.openTrain("./data/eTour/train_data/trainZ_N.txt")
    ClassiferTestTriples_Num,ClassiferTestTriples = openTxt.openTrain("./data/eTour/train_data/Classifer_test_Z.txt")
    entity_vec = []
    entity_type = []
    for triple in dkrl_train+trainZ_N:
        if triple[2] == "oracle_link":
            if stru2vec[triple[0]] not in entity_vec:
                entity_vec.append(stru2vec[triple[0]])
                entity_type.append(1)
            if stru2vec[triple[1]] not in entity_vec:
                entity_vec.append(stru2vec[triple[1]])
                entity_type.append(0)
            if cnn2vec[triple[0]] not in entity_vec:
                entity_vec.append(cnn2vec[triple[0]])
                entity_type.append(3)
            if cnn2vec[triple[1]] not in entity_vec:
                entity_vec.append(cnn2vec[triple[1]])
                entity_type.append(2)
            if stru2vec[triple[0]]+cnn2vec[triple[0]] not in entity_vec:
                entity_vec.append(stru2vec[triple[0]])
                entity_type.append(6)
            if stru2vec[triple[1]]+cnn2vec[triple[1]] not in entity_vec:
                entity_vec.append(stru2vec[triple[1]])
                entity_type.append(5)
    # x_train, y_train, x_test, y_test,x_test_triple = eTour_Experiment.orgnanizeDataFormat(dkrl_train,trainZ_N,dkrl_test,ClassiferTestTriples,cnn2vec,stru2vec,1)

    ###rp = random_projection.SparseRandomProjection(n_components=2, random_state=42)
    ###x_projected = rp.fit_transform(x_train)
    ###x_projected = decomposition.TruncatedSVD(n_components=2).fit_transform(x_train)
    ###x_projected = discriminant_analysis.LinearDiscriminantAnalysis().fit_transform(x_train, y_train)
    ###x_projected = manifold.Isomap(n_neighbors=5, n_components=2).fit_transform(x_train)
    # x_projected = manifold.LocallyLinearEmbedding(n_neighbors=30, n_components=2,
    #                                       method='hessian').fit_transform(x_train)
    ##x_projected = manifold.TSNE(n_components=2, init='pca', random_state=0).fit_transform(x_train)

    hasher = ensemble.RandomTreesEmbedding(n_estimators=200, random_state=0,
                                           max_depth=12)
    t0 = time()
    X_transformed = hasher.fit_transform(entity_vec)
    pca = decomposition.TruncatedSVD(n_components=2)
    x_projected = pca.fit_transform(X_transformed)

    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
    print(x_projected)
    xValue_1 = [x[0] for x,y in zip(x_projected,entity_type) if y ==1]
    yValue_1 = [x[1] for x,y in zip(x_projected,entity_type) if y ==1]

    xValue_0 = [x[0] for x,y in zip(x_projected,entity_type) if y ==0]
    yValue_0 = [x[1] for x,y in zip(x_projected,entity_type) if y ==0]

    xValue_3 = [x[0] for x,y in zip(x_projected,entity_type) if y ==3]
    yValue_3 = [x[1] for x,y in zip(x_projected,entity_type) if y ==3]

    xValue_2 = [x[0] for x,y in zip(x_projected,entity_type) if y ==2]
    yValue_2 = [x[1] for x,y in zip(x_projected,entity_type) if y ==2]

    xValue_6 = [x[0] for x,y in zip(x_projected,entity_type) if y ==6]
    yValue_6 = [x[1] for x,y in zip(x_projected,entity_type) if y ==6]

    xValue_5 = [x[0] for x,y in zip(x_projected,entity_type) if y ==5]
    yValue_5 = [x[1] for x,y in zip(x_projected,entity_type) if y ==5]


    plt.title(u'Entity Structure Vector Dimensionality Reduction Scatter Graph', FontProperties=font)
    plt.xlabel('x-value')
    plt.ylabel('y-value')
    # plt.scatter(x, y, s, c, marker)
    # x: x轴坐标
    # y：y轴坐标
    # s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
    # c: 点的颜色
    # marker: 标记的样式 默认是 'o'
    plt.legend()

    p1 = plt.scatter(xValue_1, yValue_1, s=25, c="b", marker="v")
    p2 = plt.scatter(xValue_0, yValue_0, s=25, c="r", marker="s")
    #p3 = plt.scatter(xValue_3, yValue_3, s=25, c="b", marker="v")
    #p4 = plt.scatter(xValue_2, yValue_2, s=25, c="r", marker="s")
    # p5 = plt.scatter(xValue_5, yValue_5, s=10, c="b", marker="v")
    # p6 = plt.scatter(xValue_6, yValue_6, s=10, c="r", marker="s")
    #plt.legend([p1, p2, p3, p4], ['Use Case Structure Vector', 'Source Code Class Structure Vector','Use Case Description Vector', 'Source Code Class Description Vector'], loc='upper right', scatterpoints=1)
    plt.legend([p1, p2], ['Use Case Structure Vector', 'Source Code Class Structure Vector'], loc='upper right', scatterpoints=1)
    #plt.legend([p3, p4], ['Use Case Description Vector', 'Source Code Class Description Vector'], loc='upper right', scatterpoints=1)
    #plt.legend([p5, p6], ['Use Case Vector', 'Source Code Class Vector'], loc='upper right', scatterpoints=1)
plt.show()
