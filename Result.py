# coding:utf-8
import numpy as np
from sklearn import metrics

'''
def get_precision(test_x, test_y, predict):
    print("len(test_x) =", len(test_x))
    print("len(test_y) =", len(test_y))
    print("len(predict) =", len(predict))

    retrieve_correct_count = 0
    for index in range(len(test_y)):
        if predict[index] == 1 and test_y[index] == 1:
            retrieve_correct_count += 1
    print("retrieve_correct_count =", retrieve_correct_count)

    total_correct_count = 0
    for index in range(len(test_y)):
        if test_y[index] == 1:
            total_correct_count += 1
    print("total_correct_count =", total_correct_count)

    total_retrieve_count = 0
    for index in range(len(test_y)):
        if predict[index] == 1:
            total_retrieve_count += 1
    print("total_retrieve_count =", total_retrieve_count)

    precision = retrieve_correct_count/total_retrieve_count
    print("precision =", precision)
    recall = retrieve_correct_count/total_correct_count
    print("recall =", recall)
'''

def get_result(test_y, predict_y):
    test_y = np.array(test_y)
    precision = metrics.precision_score(test_y, predict_y)
    recall = metrics.recall_score(test_y, predict_y)
    accuracy = metrics.accuracy_score(test_y, predict_y)
    f1_score = metrics.f1_score(test_y, predict_y)

    precision = "%.4f" % precision
    recall = "%.4f" % recall
    f1_score = "%.4f" % f1_score

    print("precision", "\t", "recall", "\t", "accuracy", "\t", "f1-score")
    print(precision, "\t", recall, "\t", accuracy, "\t", f1_score)
    return precision,recall,accuracy,f1_score
    # print("precision\trecall\taccuracy\tf1-score")
    # print(str(precision) + " "*6 + str(recall) + " "*2 + str(accuracy) + " "*7 + str(f1_score))
    # print("precision =", precision)
    # print("recall =", recall)
    # print("accuracy =", accuracy)
    # print("f1 score =", f1_score)

    # overview = metrics.classification_report(test_y, predict_y, digits=4)
    # print("overview")
    # print(overview)
