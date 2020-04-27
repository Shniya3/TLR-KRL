
def get_code_id_by_name(param_class_name):
    input_file = "../../output/eTour/relationship/class_id_name/class_id_name.txt"
    fo_read = open(input_file, "r", encoding="UTF-8")
    for line in fo_read:
        line = line.strip()
        line = line.split(" ")
        class_id = int(line[0])
        class_name = line[1]
        if class_name == param_class_name:
            return class_id

    return -1


def get_code_name_by_id(param_class_id):
    input_file = "../../output/eTour/relationship/class_id_name/class_id_name.txt"
    fo_read = open(input_file, "r", encoding="UTF-8")
    for line in fo_read:
        line = line.strip()
        line = line.split(" ")
        class_id = int(line[0])
        class_name = line[1]
        if class_id == param_class_id:
            return class_name

    return -1


def get_link_index(usecase, sourcecode):
    # the return index will not beyond the test data
    test_meta_data = PrepareData.get_test_meta_data()
    for index in range(len(test_meta_data)):
        usecase_item = test_meta_data[index]["link name"][0]
        sourcecode_item = test_meta_data[index]["link name"][1]
        if usecase == usecase_item and sourcecode == sourcecode_item:
            return index
    return -1


if __name__ == '__main__':
    class_id1 = get_code_id_by_name("BeanBeneCulturale")
    print("class_id =", class_id1)
    class_name1 = get_code_name_by_id(3)
    print("class_name =", class_name1)
