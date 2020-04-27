import SimilaritCal
import numpy as np

def getUcListCCList(tripleList):
    ucList = []
    ccList = []
    for triple in tripleList:
        if triple[2] == "oracle_link":
            if triple[0] not in ucList:
                ucList.append(triple[0])
            if triple[1] not in ccList:
                ccList.append(triple[1])
    return ucList,ccList
def IR_Rank(cnn2vec,stru2vec,dim,threshold,simFlag,DKRL_train,trainZ_N,ClassiferTest):
    print("IR Method {} start".format(simFlag))
    print(type(DKRL_train+trainZ_N+ClassiferTest))
    ucList,ccList = getUcListCCList(DKRL_train+trainZ_N+ClassiferTest)
    y_predict = [np.int32(0) for i in range(0, len(ClassiferTest))]
    for uc in ucList:
        rankList = []
        for cc in ccList:
            if (uc,cc,"oracle_link") in ClassiferTest:
                if simFlag == "cosine":
                    sim = SimilaritCal.Cosine(cnn2vec[uc],stru2vec[cc])
                rankList.append((cc,sim))
        rankList.sort(key=takeSecond,reverse=True)
        for index,tu in enumerate(rankList):
            IndexInTest = ClassiferTest.index((uc,tu[0],"oracle_link"))
            if dim == 100 and tu[1] >= threshold:
                y_predict[IndexInTest] = 1
            elif index <= dim and threshold == 1:
                y_predict[IndexInTest] = 1
            elif index <= dim and threshold >= threshold:
                y_predict[IndexInTest] = 1
            else:
                continue
    return y_predict


def takeSecond(elem):
    return elem[1]

