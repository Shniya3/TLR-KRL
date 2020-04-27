import nltk
import Tool
import openTxt
import random

if __name__ == '__main__':
    file_num,eTourCC2class = openTxt.eTourCC2class_open("./data/eTour/eTour_ea2class.txt")
    word_num,codeEntityWords = openTxt.openTrain("./data/eTour/prosessData/codeEntityWords.txt")
    word_num,codeEntity2Words = openTxt.openEntity2Des("./data/eTour/prosessData/codeEntityWords.txt")
    xmlParser_num,xmlParser = openTxt.openTrain("./data/eTour/eTour_xmlParseResult.txt")
    oracle_num,temp_oracleList = openTxt.openOracle("./data/eTour/oracle/oracle line.txt")
    ucLineNum,uc2ucLine = openTxt.openTrain("./data/eTour/prosessData/uc2ucLink.txt")
    uc_num,ucEntityWords = openTxt.openTrain("./data/eTour/prosessData/ucEntityWords.txt")
    oracleList = []
    # ucName2file = {}
    # for file in eTourCC2class:
    #     ucName2file[eTourCC2class[file]["class"][0]] = file
    # print(ucName2file["Beniculturali"])
    dirList = ["One","Two","Three"]
    crossValidationNum = 3

    for triple in temp_oracleList:
        oracleList.append((triple[0],eTourCC2class[triple[1]]["class"][0],triple[2]))
    entity_list = []
    relation_list = []
    allTrple = xmlParser+oracleList+uc2ucLine
    for triple in allTrple:
        if triple[0] not in entity_list:
            entity_list.append(triple[0])
        if triple[1] not in entity_list:
            entity_list.append(triple[1])
        if triple[2] not in relation_list:
            relation_list.append(triple[2])

    DKRL_trainZ = [triple for triple in xmlParser]+[triple for triple in uc2ucLine]
    DKRL_testZ = []
    trainZ_N = []
    Classifer_Z = []

    DKRL_trainZ_List = []
    DKRL_testZ_List = []
    trainZ_N_List = []
    Classifer_Z_List = []

    for i in range(0,crossValidationNum):
        DKRL_trainZ_List.append(DKRL_trainZ)
        DKRL_testZ_List.append([])
        trainZ_N_List.append([])
        Classifer_Z_List.append([])

    ucList = []
    ccList = []
    for triple in oracleList:
        if triple[0] not in ucList:
            ucList.append(triple[0])
        if triple[1] not in ccList:
            ccList.append(triple[1])
    for uc in ucList:
        for cc in ccList:
            randomNum = random.sample(range(0,crossValidationNum),1)[0]
            print(randomNum)
            for i in range(0,crossValidationNum):
                if i != randomNum:
                    if (uc,cc,"oracle_link") in oracleList:
                        DKRL_trainZ_List[i].append((uc,cc,"oracle_link"))
                    else:
                        trainZ_N_List[i].append((uc,cc,"oracle_link"))
                else:
                    if (uc,cc,"oracle_link") in oracleList:
                        DKRL_testZ_List[i].append((uc,cc,"oracle_link"))

                    Classifer_Z_List[i].append((uc,cc,"oracle_link"))

    for i in range(0,crossValidationNum):



        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/DKRL_trainZ.txt","w",encoding="utf-8") as w_str:
            for triple in DKRL_trainZ_List[i]:
                w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/DKRL_testZ.txt","w",encoding="utf-8") as w_str:
            for triple in DKRL_testZ_List[i]:
                w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")



        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/trainZ_N.txt","w",encoding="utf-8") as w_str:
            for triple in trainZ_N_List[i]:
                w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/Classifer_test_Z.txt","w",encoding="utf-8") as w_str:
            for triple in Classifer_Z_List[i]:
                w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")

        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/entity2id.txt","w",encoding="utf-8") as w_str:
            for index,entity in enumerate(entity_list):
                w_str.write(entity+"\t"+str(index)+"\n")
        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/relation2id.txt","w",encoding="utf-8") as w_str:
            for index,relation in enumerate(relation_list):
                w_str.write(relation+"\t"+str(index)+"\n")
        wordList = []
        stopWordList = Tool.get_stopword_list()
        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/entityWords.txt","w",encoding="utf-8") as w_str:
            for triple in codeEntityWords+ucEntityWords:
                text = triple[2]
                for codeTriple in allTrple:
                    if triple[0] == codeTriple[0] and triple[0] != codeTriple[1] and codeTriple[2] == "method":
                        if codeTriple[1] in codeEntity2Words.keys():
                            text+= (" "+codeEntity2Words[codeTriple[1]])
                new_text = ""
                tokenList = nltk.word_tokenize(text.lower())
                for w in tokenList:
                    if len(w) == 1:
                        continue
                    # elif w in stopWordList:
                    #     continue
                    new_text += (w+" ")
                    if w not in wordList:
                        wordList.append(w)
                w_str.write(triple[0]+"\t"+str(len(nltk.word_tokenize(new_text)))+"\t"+new_text+"\n")
        with open("./data/eTour/generateTrainData/CrossValidation/"+dirList[i]+"/word2id.txt","w",encoding="utf-8") as w_str:
            for index,word in enumerate(wordList):
                w_str.write(word+"\t"+str(index)+"\n")