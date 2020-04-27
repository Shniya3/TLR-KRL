
import PrepareData
import ProcessSourceCode


def capture_implements_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
            capture_implementation_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data)

            capture_interface_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict)


def capture_implementation_class_link(usecase, sourcecode, predict_y_phase2, test_meta_data):
    implementation_class_list = get_implementation_class(sourcecode)
    if len(implementation_class_list) > 0:
        for implementation_class in implementation_class_list:
            link_index = get_link_index(usecase, implementation_class)
            if link_index != -1:
                predict_y_phase2[link_index] = 1


def capture_interface_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
    interface_list = sourcecode_dict[sourcecode]["implements"]
    if len(interface_list) > 0:
        interface = interface_list[0]
        link_index = get_link_index(usecase, interface)
        if link_index != -1:
            predict_y_phase2[link_index] = 1


def capture_extends_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
            capture_subclass_link(usecase, sourcecode, predict_y_phase2, test_meta_data)

            capture_superclass_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict)


def capture_subclass_link(usecase, sourcecode, predict_y_phase2, test_meta_data):
    subclass_list = get_subclass(sourcecode)
    if len(subclass_list) > 0:
        for subclass in subclass_list:
            link_index = get_link_index(usecase, subclass)
            if link_index != -1:
                predict_y_phase2[link_index] = 1


def capture_superclass_link(usecase, sourcecode, predict_y_phase2, test_meta_data, sourcecode_dict):
    superclass_list = sourcecode_dict[sourcecode]["extends"]
    if len(superclass_list) > 0:
        superclass = superclass_list[0]
        link_index = get_link_index(usecase, superclass)
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


def get_implementation_class(interface):
    implementation_class_list = []
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    # print("sourcecode_dict =", sourcecode_dict)
    key_list = list(sourcecode_dict.keys())
    for key in key_list:
        sourcecode = sourcecode_dict[key]
        # print("sourcecode =", sourcecode)
        super_interface_list = sourcecode["implements"]
        if len(super_interface_list) > 0:
            super_interface = super_interface_list[0]
            if super_interface == interface:
                implementation_class_list.append(key)

    # print("implementation_class_list =", implementation_class_list)
    return implementation_class_list


def get_subclass(superclass_param):
    subclass_list = []
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()
    # print("sourcecode_dict =", sourcecode_dict)
    key_list = list(sourcecode_dict.keys())
    for key in key_list:
        sourcecode = sourcecode_dict[key]
        # print("sourcecode =", sourcecode)
        superclass_list= sourcecode["extends"]
        if len(superclass_list) > 0:
            superclass = superclass_list[0]
            if superclass == superclass_param:
                subclass_list.append(key)

    return subclass_list


