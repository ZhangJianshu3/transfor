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
        print lines
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

if __name__ == '__main__':
    for linenum in range(7):
        print linenum
        vecspath = 'vecspath_line' + str(linenum+1)
        x_labelpath = 'x_labelpath' + str(linenum+1)
        y_labelpath = 'y_labelpath' + str(linenum + 1)
        vecspath = '/home/wlw/projects/transfor/linetxt/pic_coor/line' + str(linenum+1)
        x_labelpath = '/home/wlw/projects/transfor/linetxt/x_coor/x_line' + str(linenum+1)
        y_labelpath = '/home/wlw/projects/transfor/linetxt/y_coor/y_line' + str(linenum+1)

        input_vecs = 'input_vecs' + str(linenum+1)
        x_labels = 'x_labels' + str(linenum+1)
        y_labels = 'y_labels' + str(linenum+1)
        input_vecs = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[0])
        x_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[1])
        y_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[2])
        print input_vecs
        print x_labels
        print y_labels
'''
    input_vecs = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[0])
    x_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[1])
    y_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[2])
    #print 'input_vecs:',input_vecs
    #print 'x_labels:',x_labels
    #print 'y_labels:',y_labels
    #读取像素坐标（u，v）、标记数据xr、yr
    u = []
    v = []
    xr = []
    yr = []
    min_ave = 10000000
    for i in input_vecs:
        u.append(i[0])
        v.append(i[1])
    for i in x_labels:
        xr.append(i)
    for i in y_labels:
        yr.append(i)
    #print 'u:',u
    #print 'v:',v
    #print 'xr:',xr
    #print 'yr:',yr
    num = 55
    seq = []          #序号集合seq[0,1,2,...54]
    for i in range(55):
        seq.append(i)
    samples = itertools.combinations(seq, 10)
    '''