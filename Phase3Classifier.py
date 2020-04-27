import Classifier_Model
import numpy as np
# import PrepareData
# import PrepareData_doc2vec

def train(train_x,train_y,test_x,test_y,select_flag):
    # train_x = []
    # train_y = []
    # test_x = []
    # test_y = []
    #
    # train_meta_data = PrepareData.get_train_meta_data()
    # test_meta_data = PrepareData.get_test_meta_data()
    # PrepareData.get_ml_data(train_meta_data, train_x, train_y)
    # PrepareData.get_ml_data(test_meta_data, test_x, test_y)

    # train_meta_data = PrepareData_doc2vec.get_train_meta_data()
    # test_meta_data = PrepareData_doc2vec.get_test_meta_data()
    # PrepareData_doc2vec.get_ml_data(train_meta_data, train_x, train_y)
    # PrepareData_doc2vec.get_ml_data(test_meta_data, test_x, test_y)

    # convert to numpy array
    train_x = np.array(train_x)
    train_y = np.array(train_y)
    test_x = np.array(test_x)
    test_y = np.array(test_y)

    # train and test
    # print("Use KNeighbors_model Classifier")
    # predict_y = Classifier_Model.KNeighbors_model(train_x, train_y, test_x)
    #
    if select_flag == 0:
        print("Use LR Classifier")
        predict_y = Classifier_Model.LogisticRegression_model(train_x, train_y, test_x)
    elif select_flag ==1:
        print("Use DT Classifier")
        predict_y = Classifier_Model.DecisionTree_model(train_x, train_y, test_x)
    elif select_flag ==2:
        print("Use SVM Classifier")
        predict_y = Classifier_Model.SVM_model_I(train_x, train_y, test_x)
    elif select_flag ==3:
        print("Use RandomForest Classifier")
        predict_y = Classifier_Model.RandomForest_model(train_x, train_y, test_x)
    elif select_flag ==4:
        print("Use GaussianNB")
        predict_y = Classifier_Model.GaussNB_model(train_x, train_y, test_x)
    elif select_flag ==5:
        print("Use MultiNB")
        predict_y = Classifier_Model.MultNB_model(train_x, train_y, test_x)
    elif select_flag ==6:
        print("GBDT")
        predict_y = Classifier_Model.GBDT_model(train_x, train_y, test_x)
    elif select_flag ==7:
        print("KNN")
        predict_y = Classifier_Model.KNeighbors_model(train_x, train_y, test_x)
    return predict_y

