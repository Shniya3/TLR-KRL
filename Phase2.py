import PrepareData
import PrepareData_doc2vec
import ProcessSourceCode
import Result
import Phase3Classifier
import Implements_Extends_Recovery
import time

def capture_more_link():
    test_x = []
    test_y = []
    test_meta_data = PrepareData.get_test_meta_data()
    PrepareData.get_ml_data(test_meta_data, test_x, test_y)

    # print("test_meta_data =", len(test_meta_data), test_meta_data)

    predict_y_phase1 = Phase3Classifier.train()
    # print("predict_y =", len(predict_y), predict_y)
    predict_y_phase1 = list(predict_y_phase1)
    predict_y_phase2 = predict_y_phase1.copy()

    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()

    for index in range(len(predict_y_phase1)):
        if predict_y_phase1[index] == 1:
            link_name = test_meta_data[index]["link name"]
            usecase = link_name[0]
            sourcecode = link_name[1]

            Implements_Extends_Recovery.capture_implements_link(usecase, sourcecode, predict_y_phase2,
                                                                test_meta_data, sourcecode_dict)

            Implements_Extends_Recovery.capture_extends_link(usecase, sourcecode, predict_y_phase2,
                                                             test_meta_data, sourcecode_dict)


    # print("test_data[20] =", len(test_data), test_data[20])
    print("phase 1 : ")
    Result.get_result(test_y, predict_y_phase1)
    tag_1_count = predict_y_phase1.count(1)
    print("capture link =", tag_1_count)
    print("phase 2 : ")
    Result.get_result(test_y, predict_y_phase2)
    tag_1_count = predict_y_phase2.count(1)
    print("capture link =", tag_1_count)


if __name__ == '__main__':
    begin_time = time.perf_counter()
    print("start")
    capture_more_link()
    end_time = time.perf_counter()
    print("Time = ", "%.2f" % (end_time - begin_time), "s")

