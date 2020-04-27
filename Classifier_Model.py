import PrepareData
import PrepareData_doc2vec
import Result
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import numpy as np

# DecisionTree
from sklearn.tree import DecisionTreeClassifier
def DecisionTree_model(train_x, train_y, test_x):
    model = DecisionTreeClassifier()
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y



# RandomForest
from sklearn.ensemble import RandomForestClassifier
def RandomForest_model(train_x, train_y, test_x):

    # param_test = {'min_samples_split':range(80,150,20), 'min_samples_leaf':range(10,60,10)}
    # grid = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 60, max_depth=13,
    #                                                        max_features='sqrt' ,oob_score=True, random_state=10),
    #                     param_grid = param_test, scoring='f1', cv=3)
    # model = grid.fit(train_x,train_y)
    param_test1 = {'n_estimators':range(10,71,10)}
    gsearch1 = GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,
                                                           min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10),
                        param_grid = param_test1, scoring='f1',cv=3)
    gsearch1.fit(train_x,train_y)

    # model = RandomForestClassifier()
    # model.fit(train_x, train_y)
    predict_y = gsearch1.predict(test_x)
    return predict_y

# GBDT(Gradient Boosting Decision Tree)
from sklearn.ensemble import GradientBoostingClassifier
def GBDT_model(train_x, train_y, test_x):
    model = GradientBoostingClassifier()
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y

# LogisticRegression
from sklearn.linear_model import LogisticRegression
def LogisticRegression_model(train_x, train_y, test_x):
    model = LogisticRegression()
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y

# KNeighbors
from sklearn.neighbors import KNeighborsClassifier
def KNeighbors_model(train_x, train_y, test_x):
    # train_x, train_y分别为训练数据集的数据和标签，test_x为测试数据
    # 默认为5
    param_grid = [
        {  # 需遍历10次
            'weights': ['uniform'], # 参数取值范围
            'n_neighbors': [i for i in range(25, 35)]  # 使用其他方式如np.arange()也可以
            # 这里没有p参数
        },
        {  # 需遍历50次
            'weights': ['distance'],
            'n_neighbors': [i for i in range(25, 35)],
            'p': [i for i in range(1, 6)]
        }
    ]
    grid_search = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=param_grid, cv=3)  # 网格搜索参数

    grid_search.fit(train_x, train_y)  # 网格搜索训练模型，比较耗时，约4分钟
    # neighbour_number = 30
    # print("neighbour_number =", neighbour_number)
    # model = KNeighborsClassifier(n_neighbors=neighbour_number)
    # model.fit(train_x, train_y)
    predict_y = grid_search.predict(test_x)
    return predict_y

# Multinomial Naive Bayes
from sklearn.naive_bayes import MultinomialNB
def MultinomialNaiveBayes_model(train_x, train_y, test_x):
    model = MultinomialNB(alpha=0.01)
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y

# SVM
from sklearn.svm import SVC
def SVM_model_grid(train_x, train_y, test_x):
    # rbf核函数，设置数据权重
    # svc = SVC(kernel='rbf', class_weight='balanced',probability=False)

    svc = SVC(kernel='poly', class_weight='balanced')
    coef = [0.0,0.1,0.2,0.3,0.4,0.5]
    c_range = np.logspace(-10, 15, 13, base=2)
    degree = [3,4,5]
    gamma_range = np.logspace(-9, 6, 11, base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉
    param_grid = [{'kernel': ["poly"], 'C': c_range, "gamma":gamma_range,"degree":degree}]
    grid = GridSearchCV(svc, param_grid,cv=3, scoring="f1",n_jobs=-1)
    # 训练模型
    model = grid.fit(train_x, train_y)
    print(model.best_estimator_)
    predict_y = model.predict(test_x)
    return predict_y

def SVM_model_I(train_x, train_y, test_x):
    model = SVC(C=0.017538469504833957, break_ties=False, cache_size=200,
                                     class_weight='balanced', coef0=0.0, decision_function_shape='ovr', degree=3,
                                     gamma=2.8284271247461903, kernel='poly', max_iter=-1, probability=True,
                                     random_state=None, shrinking=True, tol=0.001, verbose=False)
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y

def SVM_model_NI(train_x, train_y, test_x):
    model = SVC(C=32768.0, break_ties=False, cache_size=200, class_weight='balanced',
                            coef0=0.0, decision_function_shape='ovr', degree=4,
                            gamma=0.04419417382415922, kernel='poly', max_iter=-1, probability=False,
                            random_state=None, shrinking=True, tol=0.001, verbose=False)
    model.fit(train_x, train_y)
    predict_y = model.predict(test_x)
    return predict_y

from sklearn.naive_bayes import GaussianNB
def GaussNB_model(train_x, train_y, test_x):
    model = GaussianNB().fit(train_x, train_y)
    # print(model.predict_proba(test_x))
    # predict_y = []
    # for pro in model.predict_proba(test_x):
    #     if pro[1] > 0.999999:
    #         predict_y.append(np.int32(1))
    #     else:
    #         predict_y.append(np.int32(0))
    predict_y = model.predict(test_x)
    return predict_y

from sklearn.naive_bayes import MultinomialNB
def MultNB_model(train_x, train_y, test_x):
    model = MultinomialNB().fit(train_x,train_y)
    predict_y = model.predict(test_x)
    print(predict_y)
    return predict_y

def test_classifier_model():
    train_x = []
    train_y = []
    test_x = []
    test_y = []

    train_meta_data = PrepareData.get_train_meta_data()
    test_metadata = PrepareData.get_test_meta_data()
    PrepareData.get_ml_data(train_meta_data, train_x, train_y)
    PrepareData.get_ml_data(test_metadata, test_x, test_y)

    print("train correct link =", train_y.count(1))
    print("test correct link =", test_y.count(1))
    # print("precision", "\t"*3, "recall", "\t"*3, "accuracy", "\t"*3, "f1-score")
    train_x = np.array(train_x)
    train_y = np.array(train_y)
    test_x = np.array(test_x)
    test_y = np.array(test_y)

    print("capture link =", list(predict_y).count(1))

if __name__ == '__main__':
    test_classifier_model()
