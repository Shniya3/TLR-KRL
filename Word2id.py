import openTxt
if __name__ == '__main__':
    triple_num,triple_List = openTxt.openTrain("./data/entityWords.txt")
    word_list = []
    for triple in triple_List:
        for word in triple[2].strip().split(" "):
            if word not in word_list:
                word_list.append(word)

    with open("./data/word2id.txt","w",encoding="utf-8") as file:
        for index,word in enumerate(word_list):
            file.write(word+"\t"+str(index)+"\n")
