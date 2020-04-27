from math import fabs
import numpy
def TripleClassfication(train,test,y_predict,cnn2vec,stru2vec,rel2vec,rate,flag):
    print("TripleClassfication,rate:{}".format(rate))
    threshold_cnn,threshold_multi = determinationThreshold(train,cnn2vec,stru2vec,rel2vec,rate)
    y_predict = list(y_predict)
    y_predict_cnn = y_predict[:]
    y_predict_multi = y_predict[:]
    for index,triple, in enumerate(test):
        if flag:
            if y_predict[index] !=1:
                (h,t,r) = triple
                sum_cnn=cal_sum(cnn2vec[h],cnn2vec[t],rel2vec[r])
                sum_multi=cnn_stru_sum(stru2vec[h],stru2vec[t],cnn2vec[h],cnn2vec[t],rel2vec[r])
                if sum_cnn >= threshold_cnn:
                    y_predict_cnn[index] = numpy.int32(1)
                if sum_multi >= threshold_multi:
                    y_predict_multi[index] = numpy.int32(1)
        else:
            (h,t,r) = triple
            sum_cnn=cal_sum(cnn2vec[h],cnn2vec[t],rel2vec[r])
            sum_multi=cnn_stru_sum(stru2vec[h],stru2vec[t],cnn2vec[h],cnn2vec[t],rel2vec[r])
            if sum_cnn >= threshold_cnn:
                y_predict_cnn[index] = numpy.int32(1)
            if sum_multi >= threshold_multi:
                y_predict_multi[index] = numpy.int32(1)
    return y_predict_cnn,y_predict_multi

def cnn_stru_sum(h_stru,t_stru,h_cnn,t_cnn,r):
    sum = 0
    sum+=cal_sum(h_stru,t_stru,r)
    sum+=cal_sum(h_cnn,t_stru,r)
    sum+=cal_sum(h_stru,t_cnn,r)
    sum+=cal_sum(h_cnn,t_cnn,r)
    return sum

def cal_sum(h,t,r):
    sum = 0
    for i in range(0,len(h)):
        sum+=(-fabs(t[i]-h[i]-r[i]));
    return sum

def determinationThreshold(train,cnn2vec,stru2vec,rel2vec,rate):
    count_list = []
    for triple in train:
        if triple[2] == "oracle_link" and triple[0] != "EA138":
            count_list.append(triple)

    sum_cnn = 0
    sum_multi = 0
    for triple in count_list:
        (h,t,r) = triple
        sum_cnn += cal_sum(cnn2vec[h],cnn2vec[t],rel2vec[r])
        sum_multi += cnn_stru_sum(stru2vec[h],stru2vec[t],cnn2vec[h],cnn2vec[t],rel2vec[r])
    threshold_cnn = sum_cnn/len(count_list)/rate
    threshold_multi = sum_multi/len(count_list)/rate

    return threshold_cnn,threshold_multi