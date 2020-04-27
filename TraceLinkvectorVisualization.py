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

    x_train, y_train, x_test, y_test,x_test_triple = eTour_Experiment.orgnanizeDataFormat(dkrl_train,trainZ_N,dkrl_test,ClassiferTestTriples,cnn2vec,stru2vec,1)

    ###rp = random_projection.SparseRandomProjection(n_components=2, random_state=42)
    ###x_projected = rp.fit_transform(x_train)
    ###x_projected = decomposition.TruncatedSVD(n_components=2).fit_transform(x_train)
    ###x_projected = discriminant_analysis.LinearDiscriminantAnalysis().fit_transform(x_train, y_train)
    ###x_projected = manifold.Isomap(n_neighbors=5, n_components=2).fit_transform(x_train)
    # x_projected = manifold.LocallyLinearEmbedding(n_neighbors=30, n_components=2,
    #                                       method='hessian').fit_transform(x_train)
    ##x_projected = manifold.TSNE(n_components=2, init='pca', random_state=0).fit_transform(x_train)

    hasher = ensemble.RandomTreesEmbedding(n_estimators=200, random_state=0,
                                           max_depth=16)
    t0 = time()

    X_transformed = hasher.fit_transform(x_train)
    pca = decomposition.TruncatedSVD(n_components=2)
    x_projected = pca.fit_transform(X_transformed)

    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
    print(x_projected)
    xValue_1 = [x[0] for x,y in zip(x_projected,y_train) if y ==1]
    yValue_1 = [x[1] for x,y in zip(x_projected,y_train) if y ==1]

    xValue_0 = [x[0] for x,y in zip(x_projected,y_train) if y ==0]
    yValue_0 = [x[1] for x,y in zip(x_projected,y_train) if y ==0]
    # plt.title(u'Entity Vector Dimension Reduction Scatter Graph', FontProperties=font)
    plt.title(u'Traceability Link Vector Dimensionality Reduction Scatter Graph', FontProperties=font)
    plt.xlabel('x-value')
    plt.ylabel('y-value')
    # plt.scatter(x, y, s, c, marker)
    # x: x轴坐标
    # y：y轴坐标
    # s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
    # c: 点的颜色
    # marker: 标记的样式 默认是 'o'
    plt.legend()

    p1 = plt.scatter(xValue_1, yValue_1, s=10, c="b", marker="s")
    p2 = plt.scatter(xValue_0, yValue_0, s=10, c="r", marker="^")
    plt.legend([p1, p2], ['tag = 1', 'tag = 0'], loc='upper right', scatterpoints=1)

    ## plt.legend([p1, p2], ['tag = 1', 'tag = 0'], loc='upper right', scatterpoints=1)

    plt.show()
