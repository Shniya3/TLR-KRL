# coding:utf-8

import os

import Tool

def check_sourcecode_head_format():
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
            fo_read = open(os.path.join(root, file), "r", encoding="UTF-8")
            fo_read.readline()

            line2 = fo_read.readline()
            line2 = line2.strip()
            line2_array = line2.split(" : ")

            if line2_array[0] != "file name":
                print(file, " file name format wrong")
            if len(line2_array) != 2:
                print(file, " file name length wrong")

            sourcecode_filename = line2_array[1].strip()

            file_full_name = str(file)
            index = file_full_name.rfind(".")
            file_simple_name = file_full_name[:index]

            if sourcecode_filename != file_simple_name:
                print(file, " file name wrong")
                print("sourcecode_filename =", sourcecode_filename)
                print("file_simple_name =", file_simple_name)
                print("-------------------------------")

            line3 = fo_read.readline()
            line3 = line3.strip()
            line3_array = line3.split(" : ")

            if line3_array[0] != "class name":
                print(file, " class name format wrong")
            if len(line3_array) != 2:
                print(file, " class name length wrong")

            line4 = fo_read.readline()
            line4 = line4.strip()
            line4_array = line4.split(" : ")
            if line4_array[0] != "class comment":
                print(file, " class comment name wrong")
            if len(line4_array) != 2:
                print(file, " class comment length wrong")

            fo_read.close()


def check_sourcecode_implements_format():
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
            fo_read = open(os.path.join(root, file), "r", encoding="UTF-8")

            text = fo_read.read()
            text_list = text.split("---")

            overview = text_list[0].strip()

            if overview.find("implements : ") == -1:
                print(file, " don't contain implements")
            if overview.find("extends : ") == -1:
                print(file, " don't contain extends")

            overview_list = overview.split("\n")

            for line in overview_list:
                if line.find("implements :") != -1:
                    line_array = line.split(" : ")
                    if line_array[0] != "implements":
                        print(file, " implements name wrong")
                    if len(line_array) != 2:
                        print(file, " implements length wrong")

                if line.find("extends :") != -1:
                    line_array = line.split(" : ")
                    if line_array[0] != "extends":
                        print(file, " extends name wrong")
                    if len(line_array) != 2:
                        print(file, " extends length wrong")

            fo_read.close()


def check_sourcecode_u():
    sourcecode_u_list = []
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
            fo_read = open(os.path.join(root, file), "r", encoding="UTF-8")
            text = fo_read.read()
            text_list = text.split("---")
            overview = text_list[0].strip()
            if overview.find("(u)") != -1:
                sourcecode_u_list.append(file)
    print("sourcecode_u_list =", len(sourcecode_u_list), sourcecode_u_list)


def check_sourcecode_character():
    sourcecode_u_list = []
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
            fo_read = open(os.path.join(root, file), "r", encoding="UTF-8")
            text = fo_read.read()
            text_list = text.split("---")
            overview = text_list[0].strip()
            if "class : " in overview:
                sourcecode_u_list.append(file)
    print("sourcecode_u_list =", len(sourcecode_u_list), sourcecode_u_list)


def check_sourcecode_method_format():
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            for line in foRead:
                line_array = line.split(" : ")
                if len(line_array) != 2:
                    continue
                title = line_array[0]
                content = line_array[1]
                if title == "method":
                    method_list = content.split(" | ")
                    # check length
                    if len(method_list) != 4:
                        print(file, "method_list length wrong")
                    for item in method_list:
                        item_list = item.split(" - ")
                        # check length
                        if len(item_list) != 2:
                            print(file, "item_list item length wrong")
                    # check item title
                    if method_list[0].split(" - ")[0] != "method name":
                        print(file, "method name length wrong")
                    if method_list[1].split(" - ")[0] != "method parameter":
                        print(file, "method parameter length wrong")
                    if method_list[2].split(" - ")[0] != "method return":
                        print(file, "method return length wrong")
                    if method_list[3].split(" - ")[0] != "method comment":
                        print(file, "method comment length wrong")


def get_sourcecode_list():
    sourcecode_list = []
    for root, dirs, files in os.walk(output_sourcecode_directory):
        for file in files:
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            for line in foRead:
                line_array = line.split(" : ")
                title = line_array[0].strip()
                content = line_array[1].strip()
                if title == "file name":
                    sourcecode_list.append(content)

    # print("sourcecode_list length =", len(sourcecode_list), sourcecode_list)
    return sourcecode_list


def generate_sourcecode_filetype(sourcecode_directory):
    for root, dirs, files in os.walk(sourcecode_directory):
        for file in files:
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            content = foRead.read()
            content_part = content.split("---")

            info = content_part[0].strip()
            info_part = info.split("\n")

            # foWrite = open(os.path.join(root, file), "r", encoding="UTF-8")

            if str(file) == "GestioneTuristiAgenzia.txt":
                # print("info_part length =", len(info_part))
                # print("content =", content)
                print("info_part[0] =", info_part[0])
                print("info_part[1] =", info_part[1])
                print("info_part[2] =", info_part[2])
                for line in info_part:
                    line_array = line.split(" : ")
                    if len(line_array) > 0:
                        if line_array[0] == "file name":
                            print("file name =", line_array[1])

                # foWrite = open(os.path.join(root, file), "r+", encoding="UTF-8")
                #
                # foWrite.write("class type = common\n")
                # foWrite.close()


            # print("-----------------------")
            foRead.close()


def generate_sourcecode_infomation():
    for root, dirs, files in os.walk(input_sourcecode_directory):
        for file in files:
                information = ""
                output_filename = ""
                foRead = open(os.path.join(root, file), "r", encoding="UTF-8")

                text = foRead.read()
                text_list = text.split("---")

                overview = text_list[0].strip()
                overview_list = overview.split("\n")

                for line in overview_list:
                    line_array = line.split(" : ")
                    if len(line_array) != 2:
                        continue

                    title = line_array[0].strip()
                    content = line_array[1].strip()

                    if title == "file name":
                        information += "file name : " + content + "\n"
                        output_filename = content
                        continue
                    if title == "class":
                        information += "class : " + content + "\n"
                        continue
                    if title == "method":
                        method_dict = {}
                        method_information_list = content.split(" | ")
                        for item in method_information_list:
                            item = item.strip()
                            method_item = item.split(" - ")
                            method_item_title = method_item[0].strip()
                            method_item_content = method_item[1].strip()
                            
                            word_class = {}

                            remove_list = Tool.get_remove_list()
                            for item in remove_list:
                                method_item_content = method_item_content.replace(item, "")
                            method_item_content_list = method_item_content.split(" ")

                            if method_item_title == "method parameter" or method_item_title == "method return":
                                stopword_list = Tool.get_stopword_list()
                                method_item_content_list = [word for word in method_item_content_list if
                                                            word not in stopword_list]
                                word_class = {"class": method_item_content_list}

                            method_item_content_list = Tool.get_camelcase_split(method_item_content_list)
                            convert_dict = Tool.get_convert_dict()
                            for index in range(len(method_item_content_list)):
                                if method_item_content_list[index] in convert_dict:
                                    method_item_content_list[index] = convert_dict[method_item_content_list[index]]
                            for index in range(len(method_item_content_list)):
                                if method_item_content_list[index] in convert_dict:
                                    method_item_content_list[index] = convert_dict[method_item_content_list[index]]
                            stopword_list = Tool.get_stopword_list()
                            method_item_content_list = [word for word in method_item_content_list
                                                        if word not in stopword_list]

                            method_item_content_list = [word for word in method_item_content_list
                                                        if not Tool.is_number(word)]

                            if method_item_title == "method parameter" or method_item_title == "method return":
                                word_class["word"] = method_item_content_list
                                method_dict[method_item_title] = word_class
                            else:
                                method_dict[method_item_title] = method_item_content_list
                        information += "method : " + str(method_dict) + "\n"
                        continue

                    if title == "implements":
                        implements_interface_list = []
                        if content != "(none)" and content != "abcdefghijklmn":
                            implements_interface_list.append(content)
                        information += "implements : " + str(implements_interface_list) + "\n"
                        continue

                    if title == "extends":
                        extends_class_list = []
                        if content != "(none)" and content != "abcdefghijklmn":
                            extends_class_list.append(content)
                        information += "extends : " + str(extends_class_list) + "\n"
                        continue

                    
                    remove_list = Tool.get_remove_list()
                    for item in remove_list:
                        content = content.replace(item, "")

                    content_array = content.split(" ")

                    content_array = Tool.get_camelcase_split(content_array)

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

                # print("output_filename =", output_filename)
                # print("information =", information)

                output_path = output_sourcecode_directory + output_filename + ".txt"
                foWrite = open(output_path, "w", encoding="UTF-8")
                foWrite.write(information)
                foWrite.close()


def get_sourcecode_infomation():
    sourcecode_dict = {}
    for root, dirs, files in os.walk(output_sourcecode_directory):
        for file in files:
            item_dict = {}
            foRead = open(os.path.join(root, file), "r", encoding="UTF-8")
            method_list = []
            for line in foRead:
                line_array = line.split(" : ")
                title = line_array[0].strip()
                content = line_array[1].strip()
                if title == "file name":
                    key = content
                    item_dict[title] = content
                if title == "class name" or title == "class comment":
                    content = eval(content)
                    item_dict[title] = content
                if title == "implements" or title == "extends":
                    content = eval(content)
                    item_dict[title] = content
                if title == "method":
                    method_dict = eval(content)
                    method_list.append(method_dict)

            item_dict["method"] = method_list
            sourcecode_dict[key] = item_dict

    # print("sourcecode_dict =", sourcecode_dict)
    return sourcecode_dict


def get_class_type(file_name):
    file_type = "common"
    if file_name[0] == "I":
        file_type = "interface"

    return file_type


input_sourcecode_directory = "../../input/eTour/CC1/"
output_sourcecode_directory = "../../output/eTour/sourcecode/"

if __name__ == '__main__':
    # process_oracle()

    generate_sourcecode_infomation()
    # get_sourcecode_infomation()
    # get_sourcecode_list()

