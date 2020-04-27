import os
import re
import openTxt
import Tool

def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root, end=' ')  # 当前目录路径
        # print(dirs, end=' ')    # 当前路径下的所有子目录
        # print(files)            # 当前目录下的所有非目录子文件
    print(os.walk(file_dir))
    return root, dirs, files

def NameSplit(text):
    bigWord = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
               "Q","R","S","T","U","V","W","X","Y","Z"]
    newText = ""
    ContinueFlag = False
    for index,w in enumerate(text):
        if ContinueFlag:
            ContinueFlag = False
            continue
        if w in bigWord and w != "I" and w != "B" and w != "P":
            newText += ("_"+w)
        elif w == "I":
            if index+1 < len(text) and text[index+1] == "D":
                ContinueFlag = True
                newText += "_id"
            else:
                newText += ("_"+w)
        elif w == "P":
            if index+1 < len(text) and text[index+1] == "R":
                ContinueFlag = True
                newText += "_pr"
            else:
                newText += ("_"+w)
        elif w == "B":
            if index+1 < len(text) and text[index+1] == "C":
                ContinueFlag = True
                newText += "_bc"
            else:
                newText += ("_"+w)
        else:
            newText += w
    temp_list = newText.split("_")
    word_list = []
    for word in temp_list:
        if len(word) == 0:
            continue
        else:
            word_list.append(word)
    return word_list

# if __name__ == '__main__':
#     xmlParseTripleNum,xmlParseTriple = openTxt.openTrain("./data/xmlParseResult.txt")
#     code_entity_list = []
#     word_dictionary = []
#     for triple in xmlParseTriple:
#         if triple[0] not in code_entity_list:
#             code_entity_list.append(triple[0])
#         if triple[1] not in code_entity_list:
#             code_entity_list.append(triple[1])
#     code_entity_word_dict = {}
#     for entity in code_entity_list:
#         code_entity_word_dict[entity] = NameSplit(entity)
#         for word in code_entity_word_dict[entity]:
#             if word not in word_dictionary:
#                 word_dictionary.append(word)
#     print(len(word_dictionary))
#
#     word_num,word_i2e_dict = openTxt.openEntity2Des("./data/convert_word_list.txt")
#     new_code_entity_word_dict = {}
#     for key in code_entity_word_dict.keys():
#         temp_list = []
#         back_list = []
#         for word in code_entity_word_dict[key]:
#             if word in word_i2e_dict.keys():
#                 temp_list.append(word_i2e_dict[word].lower())
#             else:
#                 back_list.append(word)
#         temp_word = ""
#         for word in back_list:
#             temp_word += word
#         if temp_word in word_i2e_dict.keys():
#             temp_list.append(word_i2e_dict[temp_word])
#         new_code_entity_word_dict[key] = temp_list
#
#     with open("./data/code_entity_word_dict.txt","w",encoding="utf-8") as file:
#         for key in new_code_entity_word_dict.keys():
#             file.write(key+"\t")
#             for word in new_code_entity_word_dict[key]:
#                 file.write(word+" ")
#             file.write("\n")
#
