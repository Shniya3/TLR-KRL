import numpy as np
def EuclideanDistance(dataA,dataB):
    # np.linalg.norm 用于范数计算，默认是二范数，相当于平方和开根号
    dataA = np.mat(dataA)
    dataB = np.mat(dataB)
    return float(1.0/(1.0 + np.linalg.norm(dataA - dataB)))

def Cosine(dataA,dataB):
    dataA = np.mat(dataA)
    dataB = np.mat(dataB)
    sumData = dataA *dataB.T # 若列为向量则为 dataA.T * dataB
    denom = np.linalg.norm(dataA) * np.linalg.norm(dataB)
    # 归一化
    return float(0.5 + 0.5 * (sumData / denom))

# 余弦相似度、修正余弦相似度、皮尔逊相关系数的关系
# Pearson 减去的是每个item i 的被打分的均值
def Pearson(dataA,dataB):
    dataA = np.mat(dataA)
    dataB = np.mat(dataB)
    avgA = np.mean(dataA)
    avgB = np.mean(dataB)
    sumData = (dataA - avgA) * (dataB - avgB).T # 若列为向量则为 dataA.T * dataB
    denom = np.linalg.norm(dataA - avgA) * np.linalg.norm(dataB - avgB)
    # 归一化
    return float(0.5 + 0.5 * (sumData / denom))

# # 修正余弦相似度
# # 修正cosine 减去的是对item i打过分的每个user u，其打分的均值
# data = np.mat([[1,2,3],[3,4,5]])
# avg = np.mean(data[:,0]) # 下标0表示正在打分的用户
# def AdjustedCosine(dataA,dataB,avg):
#     sumData = (dataA - avg) * (dataB - avg).T # 若列为向量则为 dataA.T * dataB
#     denom = np.linalg.norm(dataA - avg) * np.linalg.norm(dataB - avg)
#     return 0.5 + 0.5 * (sumData / denom)
# print(AdjustedCosine(data[0,:],data[1,:],avg))