#coding:utf-8
import math
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


def get_dataset():
    # 读取数据
    # 输入向量列表，每一项是图片中的坐标
    vecspath = '/home/zjs/Projects/transfor/optimization/test/pic_test'
    x_labelpath = '/home/zjs/Projects/transfor/optimization/test/x_test'
    y_labelpath = '/home/zjs/Projects/transfor/optimization/test/y_test'
    input_vecs = get_coordinator(vecspath)
    x_labels = get_labels(x_labelpath)
    y_labels = get_labels(y_labelpath)
    #input_vecs = [[459,260], [588,262], [727,265], [890,268], [1050,274], [1218,282], [1388,293]]
    # 期望的输出列表，空间坐标，注意要与输入一一对应
    #labels = [0, 60, 120, 180, 240, 300, 360]
    return input_vecs, x_labels, y_labels


def error(xe, ye, xr, yr):
    error = []
    for i in range(0, len(xe)):
        dist = math.sqrt((xe[i]-xr[i])**2+(ye[i]-yr[i])**2)
        error.append(dist)
    return error




if __name__ == '__main__':
    input_vecs = np.array(get_dataset()[0])
    x_labels = np.array(get_dataset()[1])
    y_labels = np.array(get_dataset()[2])
    #print x
    w1 = 0.245012487727
    w2 = 0.152769676336
    b1 = -50.4548128135
    w3 = -0.0510113082818
    w4 = 0.596959007094
    b2 = -51.5904181735
    u = []
    v = []
    xr = []
    yr = []
    for i in input_vecs:
        u.append(i[0])
        v.append(i[1])
    for i in x_labels:
        xr.append(i)
    for i in y_labels:
        yr.append(i)
    xe = []
    ye = []
    i = 0
    for i in range(0, len(u)):
        xe.append(w1*u[i]+w2*v[i]+b1)
        ye.append(w3*u[i]+w4*v[i]+b2)
    print xe
    print ye
    print xr
    print yr
    error = error(xe, ye, xr, yr)
    sum = 0
    for i in error:
        sum = sum+i
    ave = sum/len(error)
    max = min = error[0]
    for i in error:
        if i <= min:
            min = i
        if i >= max:
            max = i
    print max
    print min
    print ave