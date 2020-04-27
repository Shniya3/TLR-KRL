### 返回的的dict key为实体号，内容为实体名
def openName(dir,sp="\t"):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            name_tuple = line.strip().split(sp)
            if (len(name_tuple) < 2):
                continue
            dict_[name_tuple[0]] = name_tuple[1]
            num += 1
    return num, dict_

###返回的列表存的是[实体号，实体描述]
def openDescription(dir,sp="\t"):
    num = 0
    list = []
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            des_tuple = line.strip().split(sp)
            if (len(des_tuple) < 2):
                continue
            list.append(des_tuple)
            num += 1
    return num, list

###返回的列表存的是三元组tuple
def openTrain(dir, sp="\t"):
    num = 0
    list = []
    with open(dir,encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            triple = line.strip().split(sp)
            if (len(triple) < 3):
                continue
            list.append(tuple(triple))
            num += 1
    return num, list

###返回实体列表
def openEntity_list(dir,sp='\t'):
    num = 0
    list = []
    with open(dir,encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 2):
                continue
            list.append(tuple_[0])
            num += 1
    return num, list

###返回关系列表
def openRelation_list(dir,sp='\t'):
    num = 0
    list = []
    with open(dir) as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 1):
                continue
            list.append(tuple_[0])
            num += 1
    return num, list

###返回实体to实体描述的字典
def openEntity2Des(dir,sp="\t"):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            des_tuple = line.strip().split(sp)
            if (len(des_tuple) < 3):
                continue
            dict_[des_tuple[0]] = des_tuple[2].lower()
            num += 1
    return num, dict_

###返回关系及其相关实体数
def openRelAndEnnumlist(dir,sp='\t'):
    num = 0
    list = []
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 2):
                continue
            list.append(tuple_[1])
            num += 1
    return num, list

def openTripleSent(dir,sp='\t'):
    num = 0
    list = []
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 4):
                continue
            list.append((tuple_[0],tuple_[1],tuple_[2]))
            num += 1
    return num, list

def openSememelist(dir,sp='\t'):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 2):
                continue
            dict_[tuple_[1]] = tuple_[0]
            num += 1
    return num, dict_

def openWord2Sememe(dir,sp='\t'):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 2):
                continue
            dict_[tuple_[0]] = []
            for i in range(1,len(tuple_)):
                dict_[tuple_[0]].append(tuple_[i])
            num += 1
    return num, dict_

def openRelation2Path(dir,sp='\t'):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 3):
                continue
            if tuple_[0] not in dict_.keys():
                dict_[tuple_[0]] = [(tuple_[1],tuple_[2])]
                num += 1
            else:
                if (tuple_[1],tuple_[2]) not in dict_[tuple_[0]]:
                    dict_[tuple_[0]].append((tuple_[1], tuple_[2]))
    return num, dict_

def openPath2Relation(dir,sp='\t'):
    num = 0
    dict_ = {}
    with open(dir,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 3):
                continue
            if (tuple_[1],tuple_[2]) not in dict_.keys():
                dict_[(tuple_[1],tuple_[2])] = [tuple_[0]]
                num += 1
            else:
                if tuple_[0] not in dict_[(tuple_[1],tuple_[2])]:
                    dict_[(tuple_[1], tuple_[2])].append(tuple_[0])
    return num, dict_

def openVector(dir,sp = '\t'):
    num = 0
    dict_ = {}
    with open(dir, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 3):
                continue
            if tuple_[0] not in dict_.keys():
                dict_[tuple_[0]] = [int(tuple_[i+1]) for i in range(len(tuple_)-1)]
    return num, dict_

def opemTrain_dict(dir,sp = "\t"):
    num=0
    dict_ = {}
    with open(dir, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 1):
                continue
            if tuple_[0] not in dict_.keys():
                dict_[tuple_[0]] = [(tuple_[int(2*i+1)],tuple_[int(2*i+2)]) for i in range(int((len(tuple_)-1)/2))]
    return num, dict_

def openType_spilt_dict(dir,sp = "\t"):
    num = 0,
    entity_list = []
    dict_ = {}
    with open(dir, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            tuple_ = line.strip().split(sp)
            if (len(tuple_) < 1):
                continue
            if tuple_[0] not in entity_list:
                entity_list.append(tuple_[0])
            for type in tuple_[1:len(tuple_)]:
                if type not in dict_.keys():
                    dict_[type] = []
                dict_[type].append(tuple_[0])
    return num, dict_,entity_list

def openOracle(dir, sp=" "):
    num = 0
    list = []
    with open(dir) as file:
        lines = file.readlines()
        for line in lines:
            triple = line.strip().split(sp)
            if (len(triple) < 2):
                continue
            list.append(tuple((triple[0],triple[1],"oracle_link")))
            num += 1
    return num, list

def ea2class_open(dir, sp="\t"):
    num = 0
    dict_ = {}
    with open(dir,encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            triple = line.strip().split(sp)
            if (len(triple) < 2):
                continue
            if triple[0] not in dict_.keys():
                dict_[triple[0]] = [triple[1]]
                num += 1
            else:
                dict_[triple[0]].append(triple[1])
    return num, dict_

def eTourCC2class_open(dir, sp="\t"):
    num = 0
    dict_ = {}
    with open(dir,encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            triple = line.strip().split(sp)
            if (len(triple) < 3):
                continue
            if triple[0] not in dict_.keys():
                dict_[triple[0]] = {}
            if triple[2] not in dict_[triple[0]].keys():
                dict_[triple[0]][triple[2]] = []
            dict_[triple[0]][triple[2]].append(triple[1])
            num += 1
    return num, dict_

def class2cc_open(dir, sp="\t"):
    num = 0
    dict_ = {}
    with open(dir,encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            triple = line.strip().split(sp)
            if (len(triple) < 2):
                continue
            if triple[0] not in dict_.keys():
                dict_[triple[1]] = [triple[0]]
                num += 1
            else:
                dict_[triple[1]].append(triple[0])
    return num, dict_