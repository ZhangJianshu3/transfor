#coding:utf-8
import os
import math
import itertools
import numpy as np


def get_coordinator(path):
    txtpath = path
    fp = open(txtpath)
    arr = []
    for lines in fp.readlines():
        lines = lines.replace("\n","").split(" ")
        lines = [int(i) for i in lines]
        #lines[0] = int(lines[0])
        #print lines
        arr.append(lines)
    fp.close()
    return arr

def get_labels(path):
    txtpath = path
    fp = open(txtpath)
    arr = []
    for lines in fp.readlines():
        lines = lines.replace("\n","").split(" ")
        #lines = [float(i) for i in lines]
        lines[0] = int(lines[0])
        #print lines[0]
        arr.append(lines[0])
    fp.close()
    return arr

def get_dataset(vecspath, x_labelpath, y_labelpath):
    # 构建训练数据
    # 输入向量列表，每一项是图片中的坐标
    input_vecs = get_coordinator(vecspath)
    x_labels = get_labels(x_labelpath)
    y_labels = get_labels(y_labelpath)
    #input_vecs = [[459,260], [588,262], [727,265], [890,268], [1050,274], [1218,282], [1388,293]]
    # 期望的输出列表，空间坐标，注意要与输入一一对应
    #labels = [0, 60, 120, 180, 240, 300, 360]
    return input_vecs, x_labels, y_labels

def cal_error(xe, ye, xr, yr):
    error = []
    for i in range(0, len(xe)):
        dist = math.sqrt((xe[i]-xr[i])**2+(ye[i]-yr[i])**2)
        error.append(dist)
    return error


if __name__ == '__main__':
    test_vecspath = '/home/wlw/projects/transfor/force/piece14/test/pic_test'
    test_x_labelpath = '/home/wlw/projects/transfor/force/piece14/test/x_test'
    test_y_labelpath = '/home/wlw/projects/transfor/force/piece14/test/y_test'
    test_input_vecs = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[0])
    test_x_labels = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[1])
    test_y_labels = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[2])
    #print 'input_vecs:',input_vecs
    #print 'x_labels:',x_labels
    #print 'y_labels:',y_labels
    #读取像素坐标（u，v）、标记数据xr、yr
    u = []
    v = []
    xr = []
    yr = []
    for i in test_input_vecs:
        u.append(i[0])
        v.append(i[1])
    for i in test_x_labels:
        xr.append(i)
    for i in test_y_labels:
        yr.append(i)


    vecspath = '/home/wlw/projects/transfor/force/piece14/pic_coor/balance'
    x_labelpath = '/home/wlw/projects/transfor/force/piece14/x_coor/balance_x'
    y_labelpath = '/home/wlw/projects/transfor/force/piece14/y_coor/balance_y'
    vecs_train = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[0])
    x_train = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[1])
    y_train = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[2])
    #print 'input_vecs:',vecs_train
    #print 'x_labels:',x_train
    #print 'y_labels:',y_train
    #读取像素坐标（u，v）、标记数据xr、yr

    A1 = np.column_stack([vecs_train, np.ones(len(vecs_train))])
    w1, w2, b1 = np.linalg.lstsq(A1, x_train)[0]
    print 'w1:', w1, 'w2:', w2, 'b1:', b1
    A2 = np.column_stack([vecs_train, np.ones(len(vecs_train))])
    w3, w4, b2 = np.linalg.lstsq(A2, y_train)[0]
    print 'w3:', w3, 'w4:', w4, 'b2:', b2
    # 求坐标的估计值
    xe = []
    ye = []
    i = 0
    for i in range(0, len(u)):
        xe.append(w1 * u[i] + w2 * v[i] + b1)
        ye.append(w3 * u[i] + w4 * v[i] + b2)
    # 求当前的组合的误差
    error = cal_error(xe, ye, xr, yr)
    error_path = '/home/wlw/projects/transfor/force/piece14/result/balance_error.txt'

    sum = 0
    for i in error:
        if os.path.exists(error_path):
            f = open(error_path, 'a')
            f.write(str(i)+'\n')
            f.close()
        else:
            f = open(error_path, 'w')
            f.write(str(i)+'\n')
            f.close()
        sum = sum + i
    ave = sum / len(error)
    max = min = error[0]
    for i in error:
        if i <= min:
            min = i
        if i >= max:
            max = i
    print 'max:', max
    print 'min:', min
    print 'ave:', ave

    # 将每次的结果写入txt
    data = 'balance' + ' ' + \
           str(ave) + ' ' + str(max) + ' ' + str(min) + ' ' + \
           str(w1) + ' ' + str(w2) + ' ' + str(b1) + ' ' + \
           str(w3) + ' ' + str(w4) + ' ' + str(b2) + '\n'

    txt_path = '/home/wlw/projects/transfor/force/piece14/result/piece_result.txt'
    if os.path.exists(txt_path):
        f = open(txt_path, 'a')
        f.write(data)
        f.close()
    else:
        f = open(txt_path, 'w')
        f.write(data)
        f.close()