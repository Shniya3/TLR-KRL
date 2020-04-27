import Component
from prosessData import getText
import openTxt
import nltk

if __name__ == '__main__':
    ###处理Use Case文本及生成Use Case之间的关系三元组
    root,dir,files = Component.file_path("./data/eTour/UC/")
    fileNum,fileConvert = openTxt.openName("./data/use_name_translate.txt")

    file2des = []
    uc2ucLink = []
    file2text = {}
    ucName2file = {}
    file2Name = {}
    for file in files:
        ucName, lines = getText.getETour(root+file)
        ucText = getText.subInvalidInfo(lines)
        file2Name[file.replace(".TXT","")] = ucName
        if ucName not in ucName2file.keys():
            ucName2file[ucName] = [file.replace(".txt","")]
        else:
            ucName2file[ucName].append(file.replace(".txt",""))
        file2text[file.replace(".TXT","")] = ucText
    for fileName in file2text.keys():
        for ucName in ucName2file.keys():
            if file2text[fileName].find(ucName) != -1:
                for fileName_2 in ucName2file[ucName]:
                    if fileName == fileName_2.replace(".TXT",""):
                        continue
                    uc2ucLink.append((fileName,fileName_2.replace(".TXT",""),"uc2uc_link"))
    for file in file2text.keys():
        for key in fileConvert.keys():
            file2text[file] = file2text[file].replace(file2Name[key],fileConvert[key].replace("_"," "))

    with open("./data/eTour/prosessData/uc2ucLink.txt","w",encoding="utf-8") as w_txt:
        for uc2uc in uc2ucLink:
            w_txt.write(uc2uc[0]+"\t"+uc2uc[1]+"\t"+uc2uc[2]+"\n")
    with open("./data/eTour/prosessData/uc2des.txt","w",encoding="utf-8") as w_txt:
        for file in file2text:
            w_txt.write(file+"\t"+str(len(nltk.word_tokenize(file2text[file])))+"\t"+file2text[file]+"\n")

    ###处理源代码部分

