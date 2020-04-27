 # coding:utf-8

import os

import Tool


def check_usecase_name_description_format():
    # Read all files
    for root, dirs, files in os.walk(input_usecase_directory):
        for file in files:
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")

            line1 = foRead.readline()
            line1_array = line1.split(" : ")
            if line1_array[1] != "name":
                print(file, " name format wrong")
            if len(line1_array) != 2:
                print(file, "name length wrong")

            line2 = foRead.readline()
            line2_array = line2.split(" : ")
            if line2_array[2] != "description":
                print(file, " description format wrong")
            if len(line2_array) != 2:
                print(file, "description length wrong")

            foRead.close()

def check_usecase_filename_format():
    for root, dirs, files in os.walk(input_usecase_directory):
        for file in files:
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            line1 = foRead.readline()
            line1_array = line1.split(" : ")
            if line1_array[0] != "file name":
                print(file, " file name format wrong")
            if len(line1_array) != 2:
                print(file, " file name length wrong")

            file_full_name = str(file)
            index = file_full_name.rfind(".")
            file_simple_name = file_full_name[:index]

            usecase_filename = line1_array[1].strip()

            if usecase_filename != file_simple_name:
                print(file, " file name wrong")
            # print("file_simple_name =", file_simple_name)

            foRead.close()

def generate_usecase_infomation():
    for root, dirs, files in os.walk(input_usecase_directory):
        for file in files:
                information = ""
                output_filename = ""
                foRead = open(os.path.join(root, file), "r", encoding="UTF-8")

                for line in foRead:
                    line_array = line.split(" : ")
                    if len(line_array) != 2:
                        continue
                    # print(file, "array length =", len(line_array))
                    title = line_array[0].strip()
                    content = line_array[1].strip()

                    if title == "file name":
                        information += "file name : " + content + "\n"
                        output_filename = content
                        continue

                    content = content.lower()

                    content = content.replace("(none)", "")

                    remove_list = Tool.get_remove_list()
                    for item in remove_list:
                        content = content.replace(item, "")

                    content_array = content.split(" ")

                    convert_dict = Tool.get_convert_dict()
                    for index in range(len(content_array)):
                        if content_array[index] in convert_dict:
                            content_array[index] = convert_dict[content_array[index]]
                    for index in range(len(content_array)):
                        if content_array[index] in convert_dict:
                            content_array[index] = convert_dict[content_array[index]]

                    stopword_list = Tool.get_stopword_list()
                    content_array = [word for word in content_array if word not in stopword_list]

                    content_array = [word for word in content_array if not Tool.is_number(word)]

                    information += title + " : " + str(content_array) + "\n"


                output_path = output_usecase_directory + output_filename + ".txt"
                foWrite = open(output_path, "w", encoding="UTF-8")
                foWrite.write(information)
                foWrite.close()

def get_usecase_infomation():
    usecase_dict = {}
    for root, dirs, files in os.walk(output_usecase_directory):
        for file in files:
            item_dict = {}
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            for line in foRead:
                line_array = line.split(" : ")
                title = line_array[0].strip()
                content = line_array[1].strip()
                if title == "file name":
                    key = content
                if title == "name" or title == "description":
                    content = eval(content)

                item_dict[title] = content

            usecase_dict[key] = item_dict

    # print("usecase_dict =", usecase_dict)
    return usecase_dict


input_usecase_directory = "../../input/eTOUR/UC1/"
output_usecase_directory = "../../output/eTour/usecase/"

if __name__ == '__main__':

    generate_usecase_infomation()
    # get_usecase_infomation()

