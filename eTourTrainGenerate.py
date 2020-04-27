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
    print(eTourCC2class)
    print(temp_oracleList)
    for triple in temp_oracleList:
        oracleList.append((triple[0],eTourCC2class[triple[1]]["class"][0],triple[2]))
    print(oracleList)
    # entityList,relationList
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
    DKRL_trainW = [triple for triple in xmlParser]+[triple for triple in uc2ucLine]
    trainW_N = []
    DKRL_testW = []
    Classifer_W = []

    DKRL_trainZ = [triple for triple in xmlParser]+[triple for triple in uc2ucLine]
    DKRL_testZ = []
    trainZ_N = []
    Classifer_Z = []
    ucList = []
    ccList = []
    for triple in oracleList:
        if triple[0] not in ucList:
            ucList.append(triple[0])
        if triple[1] not in ccList:
            ccList.append(triple[1])
    for uc in ucList:
        for cc in ccList:
            randomNum = random.random()
            if random.random() < 3500/6728:
                if random.random() < 4/7:
                    if (uc,cc,"oracle_link") in oracleList:
                        DKRL_trainW.append((uc,cc,"oracle_link"))
                    else:
                        trainW_N.append((uc,cc,"oracle_link"))
                else:
                    if (uc,cc,"oracle_link") in oracleList:
                        DKRL_testW.append((uc,cc,"oracle_link"))

                    Classifer_W.append((uc,cc,"oracle_link"))
            if random.random() < 4/7:
                if (uc,cc,"oracle_link") in oracleList:
                    DKRL_trainZ.append((uc,cc,"oracle_link"))
                else:
                    trainZ_N.append((uc,cc,"oracle_link"))
            else:
                if (uc,cc,"oracle_link") in oracleList:
                    DKRL_testZ.append((uc,cc,"oracle_link"))

                Classifer_Z.append((uc,cc,"oracle_link"))
    with open("./data/eTour/generateTrainData/DKRL_trainZ.txt","w",encoding="utf-8") as w_str:
        for triple in DKRL_trainZ:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/DKRL_testZ.txt","w",encoding="utf-8") as w_str:
        for triple in DKRL_testZ:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/DKRL_trainW.txt","w",encoding="utf-8") as w_str:
        for triple in DKRL_trainW:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/DKRL_testW.txt","w",encoding="utf-8") as w_str:
        for triple in DKRL_testW:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")

    with open("./data/eTour/generateTrainData/trainW_N.txt","w",encoding="utf-8") as w_str:
        for triple in trainW_N:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/Classifer_test_W.txt","w",encoding="utf-8") as w_str:
        for triple in Classifer_W:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/trainZ_N.txt","w",encoding="utf-8") as w_str:
        for triple in trainZ_N:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")
    with open("./data/eTour/generateTrainData/Classifer_test_Z.txt","w",encoding="utf-8") as w_str:
        for triple in Classifer_Z:
            w_str.write(triple[0]+"\t"+triple[1]+"\t"+triple[2]+"\n")

    with open("./data/eTour/generateTrainData/entity2id.txt","w",encoding="utf-8") as w_str:
        for index,entity in enumerate(entity_list):
            w_str.write(entity+"\t"+str(index)+"\n")
    with open("./data/eTour/generateTrainData/relation2id.txt","w",encoding="utf-8") as w_str:
        for index,relation in enumerate(relation_list):
            w_str.write(relation+"\t"+str(index)+"\n")
    wordList = []
    stopWordList = Tool.get_stopword_list()
    with open("./data/eTour/generateTrainData/entityWords.txt","w",encoding="utf-8") as w_str:
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
    with open("./data/eTour/generateTrainData/word2id.txt","w",encoding="utf-8") as w_str:
        for index,word in enumerate(wordList):
            w_str.write(word+"\t"+str(index)+"\n")