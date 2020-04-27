import os
import numpy as np
def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root, end=' ')  # 当前目录路径
        # print(dirs, end=' ')    # 当前路径下的所有子目录
        # print(files)            # 当前目录下的所有非目录子文件
    print(os.walk(file_dir))
    return root, dirs, files

def takeSecond(elem):
    return elem[1]

def scoreToPredict(threshold,y_score):
    y_predict = []
    for score in y_score:
        if score >threshold:
            y_predict.append(np.int32(1))
        else:
            y_predict.append(np.int32(0))
    return y_predict
