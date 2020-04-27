import nltk
import NameSplit
import openTxt
import Tool
import re

if __name__ == '__main__':
    class_num,class2comment = openTxt.openDescription("./data/eTour/class2comment.txt")
    file_num,eTourCC2class = openTxt.eTourCC2class_open("./data/eTour/eTour_ea2class.txt")
    entity_num,entity2word = openTxt.openEntity2Des("./data/eTour/code_entity_word_dict.txt")
    word_num,temp_word_i2e_dict = openTxt.openEntity2Des("./data/convert_word_list.txt")
    uc_num,ucEntityWords = openTxt.openTrain("./data/eTour/prosessData/uc2des.txt")

    word_i2e_dict = {}
    saveEnglish = re.compile("[^a-zA-Z]")
    classList = [tu[0] for tu in class2comment]
    for key in entity2word:
        if key in classList:
            index = classList.index(key)
            class2comment[index][1] += (" "+key)
        else:
            class2comment.append((key,key))

    for key in temp_word_i2e_dict.keys():
        if key not in word_i2e_dict.keys():
            word_i2e_dict[key] = temp_word_i2e_dict[key]
        if key.lower() not in word_i2e_dict.keys():
            word_i2e_dict[key.lower()] = temp_word_i2e_dict[key]
        if key.capitalize() not in word_i2e_dict.keys():
            word_i2e_dict[key.capitalize()] = temp_word_i2e_dict[key]

    with open("./data/eTour/prosessData/codeEntityWords.txt","w",encoding="utf-8") as w_str:
        for enDes_tuple in class2comment:
            temp = ""
            for word in nltk.word_tokenize(enDes_tuple[1]):

                # if word in entity2word.keys():
                #     word = entity2word[word]
                #     temp += (word+" ")
                if word in word_i2e_dict.keys():
                    temp += (word_i2e_dict[word]+" ")
                elif word.lower() in word_i2e_dict.keys():
                    temp += (word_i2e_dict[word.lower()]+" ")
                elif len(NameSplit.NameSplit(word)) != 1:
                    for w in NameSplit.NameSplit(word):
                        if w in word_i2e_dict.keys():
                            temp += (word_i2e_dict[w]+" ")
                        else:
                            temp += (w+" ")

                else:
                    temp += (word+" ")
            if enDes_tuple[0] != enDes_tuple[1]:

                record = len(nltk.word_tokenize(temp))/len(NameSplit.NameSplit(enDes_tuple[0]))
                if record <= 1:
                    for word in NameSplit.NameSplit(enDes_tuple[0]):
                        for w in NameSplit.NameSplit(word):
                            if w in word_i2e_dict.keys():
                                temp += (word_i2e_dict[w]+" ")
                            else:
                                temp += (w+" ")
                else:
                    for i in range(0,int(record)):
                        for word in NameSplit.NameSplit(enDes_tuple[0]):
                            for w in NameSplit.NameSplit(word):
                                if w in word_i2e_dict.keys():
                                    temp += (word_i2e_dict[w]+" ")
                                else:
                                    temp += (w+" ")
            # print(enDes_tuple[1])
            # print(temp)
            temp_2 = ""
            for word in nltk.word_tokenize(temp):
                temp_2 += (saveEnglish.sub(" " , word)+" ")
            temp_3 = ""
            for word in nltk.word_tokenize(temp_2):
                if len(word) == 1:
                    continue
                temp_3 += (word+" ")
            w_str.write(enDes_tuple[0]+"\t"+str(len(nltk.word_tokenize(temp_3)))+"\t"+temp_3+"\n")


    with open("./data/eTour/prosessData/ucEntityWords.txt","w",encoding="utf-8") as w_str:
        for ucDesTuple in ucEntityWords:
            print(ucDesTuple)
            temp = ""
            for word in nltk.word_tokenize(ucDesTuple[2]):
                temp += (saveEnglish.sub(" " , word)+" ")
            print(temp)
            temp2 = ""
            for word in nltk.word_tokenize(temp):
                for w in NameSplit.NameSplit(word):
                    if w in word_i2e_dict.keys():
                        temp2 += (word_i2e_dict[w]+" ")
                    else:
                        temp2 += (w+" ")
            print("temp2:{}".format(temp2))
            temp3 = ""
            for word in nltk.word_tokenize(temp2):
                print(word)
                if len(word) == 1:

                    continue
                temp3 += (word+" ")
            print(temp3)
            w_str.write(ucDesTuple[0]+"\t"+str(len(nltk.word_tokenize(temp3)))+"\t"+temp3+"\n")

