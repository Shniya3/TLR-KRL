
import PrepareData
import ProcessSourceCode


def capture_parameter_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
            capture_class_parameter_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict)

            capture_parameter_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data)


def capture_class_parameter_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
    sourcecode_parameter_list = []
    method_list = sourcecode_dict[sourcecode]["method"]
    for method in method_list:
        parameter_class_list = method["method parameter"]["class"]
        if len(parameter_class_list) > 0:
            sourcecode_parameter_list.extend(parameter_class_list)
    for parameter_class in sourcecode_parameter_list:
        link_index = get_link_index(usecase, parameter_class)
        if link_index != -1:
            predict_y_phase2[link_index] = 1


def capture_parameter_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data):
    class_list = get_class_parameter(sourcecode)
    for class_item in class_list:
        link_index = get_link_index(usecase, class_item)
        if link_index != -1:
            predict_y_phase2[link_index] = 1


def capture_return_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
            capture_class_return_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict)

            capture_return_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data)


def capture_class_return_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
    sourcecode_return_list = []
    method_list = sourcecode_dict[sourcecode]["method"]
    if len(method_list) > 0:
        for method in method_list:
            return_class_list = method["method return"]["class"]
            if len(return_class_list) > 0:
                sourcecode_return_list.extend(return_class_list)
    for return_class in sourcecode_return_list:
        link_index = get_link_index(usecase, return_class)
        if link_index != -1:
            predict_y_phase2[link_index] = 1


def capture_return_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data):
    class_list = get_class_return(sourcecode)
    for class_item in class_list:
        link_index = get_link_index(usecase, class_item)
        if link_index != -1:
            predict_y_phase2[link_index] = 1


def get_link_index(usecase, sourcecode):
    test_meta_data = PrepareData.get_test_meta_data()
    for index in range(len(test_meta_data)):
        usecase_item = test_meta_data[index]["link name"][0]
        sourcecode_item = test_meta_data[index]["link name"][1]
        if usecase == usecase_item and sourcecode == sourcecode_item:
            return index
    return -1


def get_class_parameter(parameter_param):
    class_list = []
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    # print("sourcecode_dict =", sourcecode_dict)
    key_list = list(sourcecode_dict.keys())
    for key in key_list:
        sourcecode = sourcecode_dict[key]
        method_list = sourcecode["method"]
        for method in method_list:
            method_parameter_list = method["method parameter"]["class"]
            for class_type in method_parameter_list:
                if class_type == parameter_param:
                    class_list.append(key)
                    break

    return class_list


def get_class_return(return_param):
    class_list = []
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    # print("sourcecode_dict =", sourcecode_dict)
    key_list = list(sourcecode_dict.keys())
    for key in key_list:
        sourcecode = sourcecode_dict[key]
        method_list = sourcecode["method"]
        for method in method_list:
            method_return_list = method["method return"]["class"]
            for class_type in method_return_list:
                if class_type == return_param:
                    class_list.append(key)
                    break

    return class_list


