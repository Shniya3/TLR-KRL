import re
import nltk
import os
import csv

from pip._vendor import chardet

import openTxt


def comment_extractt(root,file, cc2class):

    dir = root+file
    if cc2class["class"][0] == "":
        with open("./data/eTour/error_code/error.txt","a",encoding="utf-8") as w_str:
            w_str.write(file+"\n")
        return False
    class_list = cc2class["class"]
    # if "method" in cc2class.keys():
    print(cc2class)
    if "method" in cc2class.keys():
        class_list += cc2class["method"]
    # if "field" in cc2class.keys():
    #     class_list += cc2class["field"]
    object2comment_dict = {}
    with open(dir, encoding="utf-8") as file:
        lines = file.readlines()
    break_flag_1 = False
    break_flag_2 = False
    ###存/* */
    record_list_2 = []
    record_1 = 0
    for record_index, line in enumerate(lines):
        if line. find("/ *") is not -1 and line.find("* /") is not -1:
            record_4 = record_index
            for index in range(len(lines)-1,-1,-1):
                line_4 = lines[index]
                if break_flag_2 is True:
                    break_flag_2 = False
                    break
                if index < record_4:
                    for class_object in class_list:
                        if line_4.find(class_object) is not -1:
                            if class_object in object2comment_dict.keys():
                                object2comment_dict[class_object] += lines[record_4]
                            else:
                                object2comment_dict[class_object] = ""
                                object2comment_dict[class_object] += lines[record_4]
                            break_flag_2 = True
                            break
        elif line.find("/ *") is not -1 and line.find("/ / *") is -1:
            record_list_2.append(record_index)
            record_1 = record_index
        elif line.find("* /") is not -1:
            record_list_2.append(record_index)
            record_2 = record_index
            if record_2 > record_1:
                for index, line_2 in enumerate(lines):
                    if break_flag_1 is True:
                        break_flag_1 = False
                        break
                    if index > record_2 :
                        for class_object in class_list:
                            if line_2.find(class_object) is not -1:
                                if class_object in object2comment_dict.keys():
                                    for text in lines[record_1:(record_2+1)]:
                                        object2comment_dict[class_object] += text
                                else:
                                    object2comment_dict[class_object] = ""
                                    for text in lines[record_1:(record_2+1)]:
                                        object2comment_dict[class_object] += text
                                break_flag_1 = True
                                break


        elif line.find("/ /") is not -1:
            record_3 = record_index

            for index in range(len(lines)-1,-1,-1):
                line_3 = lines[index]
                if break_flag_2 is True:
                    break_flag_2 = False
                    break
                if index < record_3:
                    for class_object in class_list:
                        if line_3.find(class_object) is not -1:
                            if class_object in object2comment_dict.keys():
                                object2comment_dict[class_object] += lines[record_3]
                            else:
                                object2comment_dict[class_object] = ""
                                object2comment_dict[class_object] += lines[record_3]
                            break_flag_2 = True
                            break

    if len(record_list_2) % 2 is not 0:
        return False

    return object2comment_dict


def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root, end=' ')  # 当前目录路径
        # print(dirs, end=' ')    # 当前路径下的所有子目录
        # print(files)            # 当前目录下的所有非目录子文件
    print(os.walk(file_dir))
    return root, dirs, files



if __name__ == '__main__':

    # with open('./data/CC/EA140.txt', 'rb') as file:
    #     print(chardet.detect(file.read())) # {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
    #     a=file.readlines()
    #     print(a)

    root, dirs, files = file_path("./data/eTour/CC/")
    record = []
    class_num,eTourCC2class = openTxt.eTourCC2class_open("./data/eTour/eTour_ea2class.txt")
    comment_dict = {}
    for file in files:
        print(file)
        class2comment_dict = comment_extractt(root,file, eTourCC2class[file.replace(".txt","")])
        print(class2comment_dict)
        if class2comment_dict:
            for key in class2comment_dict.keys():
                if key not in comment_dict:
                    comment_dict[key] = class2comment_dict[key]
                else:
                    comment_dict[key] += class2comment_dict[key]
    with open("./data/eTour/class2comment.txt","w",encoding="utf-8") as file:
        for key in comment_dict:
            file.write(key+"\t"+(comment_dict[key].replace("\t","").replace("\n","").replace("/ *","").replace("* /","").replace("/ /","").replace("*","").replace("@",""))+"\n")



