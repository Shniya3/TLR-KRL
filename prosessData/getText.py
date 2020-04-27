import nltk
import re
def getETour(dir):
    clean = re.compile("[^a-zA-Z\s]")
    useCaseName = re.compile("Use case name (.*?) ")
    with open(dir,"r",encoding="utf-8") as file:
        lines = file.readlines()
    line_all = ""
    for line in lines:
        line_all+= line
    line_all = clean.sub(" ",line_all,)
    lines = nltk.word_tokenize(line_all)
    line_all = ""
    for word in lines:
        line_all += (word+" ")
    return useCaseName.findall(line_all)[0], line_all


def subInvalidInfo(text):
    text = text.replace("Use case name","")
    text = text.replace("Partecipating","")
    text = text.replace("Participating","")
    text = text.replace("Entry Operator conditions","")
    text = text.replace("Entry conditions","")
    text = text.replace("Flow of events User System","")
    text = text.replace("Flow of events Gps System","")
    text = text.replace("Exit conditions","")
    text = text.replace("Quality requirements","")
    text = text.replace("Quality","")
    temp = ""
    for word in nltk.word_tokenize(text):
        temp += (word + " ")
    return temp
