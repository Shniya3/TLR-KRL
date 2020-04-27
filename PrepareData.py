coding:utf-8

import ProcessUseCase
import ProcessSourceCode
import ProcessOracle

def get_meta_linklist():
    # get oracle list
    oracle_list = ProcessOracle.get_oracle_list()

    usecase_dict = ProcessUseCase.get_usecase_infomation()
    sourcecode_dict = ProcessSourceCode.get_sourcecode_infomation()

    usecase_dict_keys = list(usecase_dict.keys())
    sourcecode_dict_keys = list(sourcecode_dict.keys())

    link_list = []
    for usecase_key in usecase_dict_keys:
        usecase = usecase_dict[usecase_key]
        usecase_filename = usecase["file name"]
        usecase_name_list = usecase["name"]
        usecase_description_list = usecase["description"]
        for sourcecode_key in sourcecode_dict_keys:
            link = {}
            sourcecode = sourcecode_dict[sourcecode_key]
            sourcecode_filename = sourcecode["file name"]
            sourcecode_classname_list = sourcecode["class name"]
            sourcecode_classcomment_list = sourcecode["class comment"]
            sourcecode_method_list = sourcecode["method"]

            count1 = 0
            count2 = 0
            for word in sourcecode_classname_list:
                if word in usecase_name_list:
                    count1 += 1
                if word in usecase_description_list:
                    count2 += 1

            count3 = 0
            count4 = 0
            for word in sourcecode_classcomment_list:
                if word in usecase_name_list:
                    count3 += 1
                if word in usecase_description_list:
                    count4 += 1

            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0
            count9 = 0
            count10 = 0
            count11 = 0
            count12 = 0

            for method in sourcecode_method_list:
                method_name_list = method["method name"]
                method_comment_list = method["method comment"]
                method_parameter_list = method["method parameter"]["word"]
                method_return_list = method["method return"]["word"]
                for word in method_name_list:
                    if word in usecase_name_list:
                        count5 += 1
                    if word in usecase_description_list:
                        count6 += 1
                for word in method_comment_list:
                    if word in usecase_name_list:
                        count7 += 1
                    if word in usecase_description_list:
                        count8 += 1

                for word in method_parameter_list:
                    if word in usecase_name_list:
                        count9 += 1
                    if word in usecase_description_list:
                        count10 += 1

                for word in method_return_list:
                    if word in usecase_name_list:
                        count11 += 1
                    if word in usecase_description_list:
                        count12 += 1

            link["link name"] = [usecase_filename, sourcecode_filename]
            vector = [count1, count2, count3, count4]
            vector.extend([count5, count6, count7, count8])
            vector.extend([count9, count10, count11, count12])
            link["link vector"] = vector
            if link["link name"] in oracle_list:
                link["link flag"] = True
            else:
                link["link flag"] = False
            link_list.append(link)

    # print("link_list length =", len(link_list), link_list)
    return link_list

# def get_oracle_vector():
#     # oracle_vector = []
#     link_list = get_meta_linklist()
#     for link in link_list:
#         if link["link flag"] is True:
#             print(link["link name"], "=", link["link vector"])
#     # for link in link_list:
#     #     if link["link flag"] is False:
#     #         print(link["link name"], "=", link["link vector"])


train_begin_index = 2000
train_end_index = 4000
test_begin_index = 500
test_end_index = 2000

def get_train_meta_data():
    link_list = get_meta_linklist()
    train_data = link_list[train_begin_index:train_end_index]
    return train_data

def get_test_meta_data():
    link_list = get_meta_linklist()
    test_data = link_list[test_begin_index:test_end_index]
    return test_data

def get_ml_data(meta_link_list, x_data, y_data):
    # print("meta_link_list =", len(meta_link_list), meta_link_list[20])
    for link in meta_link_list:
        link_vector = link["link vector"]

        link_flag = link["link flag"]
        if link_flag is True:
            link_tag = 1
        if link_flag is False:
            link_tag = 0
        x_data.append(link_vector)
        y_data.append(link_tag)
    
def get_oracle_data():
    oracle_data = []
    link_list = get_meta_linklist()
    for link in link_list:
        if link["link flag"] is True:
            oracle_data.append(link["link vector"])
            print(link["link name"], "=", link["link vector"])

    # print("oracle_data =", oracle_data)
    return oracle_data

def get_nonlink_data():
    nonlink_data = []
    link_list = get_meta_linklist()
    for link in link_list:
        if link["link flag"] is False:
            nonlink_data.append(link["link vector"])
            print(link["link name"], "=", link["link vector"])

    return nonlink_data

