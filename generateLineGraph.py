import numpy as np
import csv
if __name__ == '__main__':
    with open("./data/eTour/experimentResult.txt","r",encoding="utf-8") as file:
        lines = file.readlines()
        resultList = []
        for line in lines:
            tu_ = line.strip().split("\t")
            if len(tu_)<4:
                continue
            resultList.append((float(tu_[0]),float(tu_[1]),float(tu_[2]),float(tu_[3])))
    print(resultList)
    cleanResult = []
    recallRanges = [0.585,0.615]### np.linspace(0,1,20) ##
    print(recallRanges)
    recordDict = {}
    for recallRange in recallRanges:
        recordDict[recallRange] = 0
    for resultIndex,result in enumerate(resultList):
        if result[1]>0.585 and result[1]<0.615:
            if result[3]>resultList[recordDict[recallRange]][3]:
                recordDict[recallRange] = resultIndex
                print(resultList[resultIndex])
        # for index,recallRange in enumerate(recallRanges):
        #     if result[1]>recallRange and result[1]<recallRanges[index+1]:
        #         if result[3]>resultList[recordDict[recallRange]][3]:
        #             recordDict[recallRange] = resultIndex
    for key in recordDict.keys():
        cleanResult.append(resultList[recordDict[key]])
    with open("./data/eTour/experimentCleanResult.csv","w",encoding="utf-8",newline="") as w_csv:
        writer = csv.writer(w_csv)
        writer.writerows(cleanResult)