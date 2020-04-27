import numpy


def LogicalReasoning(train,x_test_triple,y_predict,inheritFlag,implementsFlag,parameterFlag,returnFlag):
    if inheritFlag:
        return ReasonInherit(train,x_test_triple,y_predict)
    if implementsFlag:
        return ReasonImplements(train,x_test_triple,y_predict)
    if parameterFlag:
        return ReasonParameter(train,x_test_triple,y_predict)
    if returnFlag:
        return ReasonReturn(train,x_test_triple,y_predict)

def ReasonInherit(train,x_test_triple,y_predict_in):
    y_predict = list(y_predict_in)
    print("inherit reasoning")
    evidence = train
    # for predict_triple,predict_val in zip(x_test_triple,y_predict):
    #     if predict_val == 1:
    #         evidence.append(predict_triple)
    reasonResult = []
    for eviTriple in evidence:
        if eviTriple[2] == "oracle_link":
            for triple in evidence:
                if triple[1] == eviTriple[1] and triple[2] == "super_class":
                    reasonResult.append((eviTriple[0],triple[0],eviTriple[2]))
    for resTriple in reasonResult:
        if resTriple in x_test_triple:
            y_predict[x_test_triple.index(resTriple)] = numpy.int32(1)
    return y_predict

def ReasonImplements(train,x_test_triple,y_predict_in):
    y_predict = list(y_predict_in)
    print("implements reasoning")
    evidence = train
    for predict_triple,predict_val in zip(x_test_triple,y_predict):
        if predict_val == 1:
            evidence.append(predict_triple)
    reasonResult = []
    for eviTriple in evidence:
        if eviTriple[2] == "oracle_link":
            for triple in evidence:
                if triple[1] == eviTriple[1] and triple[2] == "super_interface":
                    reasonResult.append((eviTriple[0],triple[0],eviTriple[2]))
    for resTriple in reasonResult:
        if resTriple in x_test_triple:
            y_predict[x_test_triple.index(resTriple)] = numpy.int32(1)
    return y_predict

def ReasonParameter(train,x_test_triple,y_predict_in):
    y_predict = list(y_predict_in)
    print("parameter type reasoning")
    evidence = train
    for predict_triple,predict_val in zip(x_test_triple,y_predict):
        if predict_val == 1:
            evidence.append(predict_triple)
    reasonResult = []
    ###method Parameter Type Dict
    class2ParameterTypeDict = {}
    for triple in evidence:
        if triple[2] == "method":
            if triple[0] not in class2ParameterTypeDict.keys():
                class2ParameterTypeDict[triple[0]] = []
            for triple2 in evidence:
                if triple2[0] == triple[1] and triple2[2] == "parameter":
                    if triple2[1] not in class2ParameterTypeDict[triple[0]]:
                        class2ParameterTypeDict[triple[0]].append(triple2[1])

    for eviTriple in evidence:
        if eviTriple[2] == "oracle_link":
            if eviTriple[1] in class2ParameterTypeDict.keys() and len(class2ParameterTypeDict[eviTriple[1]]) > 0:
                for parameterType in class2ParameterTypeDict[eviTriple[1]]:
                    reasonResult.append((eviTriple[0],parameterType,eviTriple[2]))

    for resTriple in reasonResult:
        if resTriple in x_test_triple:
            y_predict[x_test_triple.index(resTriple)] = numpy.int32(1)
    return y_predict

def ReasonReturn(train,x_test_triple,y_predict_in):
    y_predict = list(y_predict_in)
    print("return type reasoning")
    evidence = train
    for predict_triple,predict_val in zip(x_test_triple,y_predict):
        if predict_val == 1:
            evidence.append(predict_triple)
    reasonResult = []
    class2ReturnTypeDict = {}
    for triple in evidence:
        if triple[2] == "method":
            if triple[0] not in class2ReturnTypeDict.keys():
                class2ReturnTypeDict[triple[0]] = []
            for triple2 in evidence:
                if triple2[0] == triple[1] and triple2[2] == "return_type":
                    if triple2[1] not in class2ReturnTypeDict[triple[0]]:
                        class2ReturnTypeDict[triple[0]].append(triple2[1])

    for eviTriple in evidence:
        if eviTriple[2] == "oracle_link":
            if eviTriple[1] in class2ReturnTypeDict.keys() and len(class2ReturnTypeDict[eviTriple[1]]) > 0:
                for returnType in class2ReturnTypeDict[eviTriple[1]]:
                    reasonResult.append((eviTriple[0],returnType,eviTriple[2]))

    for resTriple in reasonResult:
        if resTriple in x_test_triple:
            y_predict[x_test_triple.index(resTriple)] = numpy.int32(1)
    return y_predict