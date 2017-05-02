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
    test_vecspath = '/home/wlw/projects/transfor/pic_test'
    test_x_labelpath = '/home/wlw/projects/transfor/x_test'
    test_y_labelpath = '/home/wlw/projects/transfor/y_test'
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
    min_ave = 10000000
    for i in test_input_vecs:
        u.append(i[0])
        v.append(i[1])
    for i in test_x_labels:
        xr.append(i)
    for i in test_y_labels:
        yr.append(i)

    num = 8
    seq = []  # 序号集合seq[0,1,2,...8]
    for i in range(8):
        seq.append(i)
    samples = itertools.combinations(seq, 4)
    for sample in samples:
        print sample
        vecs_train = []
        x_train = []
        y_train = []

        for linenum in range(7):
            #print linenum
            vecspath = 'vecspath_line' + str(linenum+1)
            x_labelpath = 'x_labelpath' + str(linenum+1)
            y_labelpath = 'y_labelpath' + str(linenum + 1)
            vecspath = '/home/wlw/projects/transfor/force/linetxt/pic_coor/line' + str(linenum+1)
            x_labelpath = '/home/wlw/projects/transfor/force/linetxt/x_coor/x_line' + str(linenum+1)
            y_labelpath = '/home/wlw/projects/transfor/force/linetxt/y_coor/y_line' + str(linenum+1)

            input_vecs = 'input_vecs' + str(linenum+1)
            x_labels = 'x_labels' + str(linenum+1)
            y_labels = 'y_labels' + str(linenum+1)
            input_vecs = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[0])
            x_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[1])
            y_labels = np.array(get_dataset(vecspath, x_labelpath, y_labelpath)[2])
            #print input_vecs
            #print x_labels
            #print y_labels
            for num in sample:
                vecs_train.append(input_vecs[num])
                x_train.append(x_labels[num])
                y_train.append(y_labels[num])
        print 'x',x_train
        print 'y',y_train
        # 线性回归
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
        '''
        print 'xe:',xe
        print 'ye:',ye
        print 'xr:',xr
        print 'yr:',yr
        '''
        # 求当前的组合的误差
        error = cal_error(xe, ye, xr, yr)
        sum = 0
        for i in error:
            sum = sum + i
        ave = sum / len(error)
        max = min = error[0]
        for i in error:
            if i <= min:
                min = i
            if i >= max:
                max = i
        if ave < min_ave:
            min_ave = ave
            min_seq = sample
            min_w1 = w1
            min_w2 = w2
            min_b1 = b1
            min_w3 = w3
            min_w4 = w4
            min_b2 = b2
        print 'max:', max
        print 'min:', min
        print 'ave:', ave
        print 'min_ave', min_ave
        print 'min_seq', min_seq
        # 将每次的结果写入txt
        data = str(sample) + ' ' + \
               str(ave) + ' ' + str(max) + ' ' + str(min) + ' ' + \
               str(w1) + ' ' + str(w2) + ' ' + str(b1) + ' ' + \
               str(w3) + ' ' + str(w4) + ' ' + str(b2) + '\n'
        txt_path = '/home/wlw/projects/transfor/force_result/sort/28_in_56.txt'
        if os.path.exists(txt_path):
            f = open(txt_path, 'a')
            f.write(data)
            f.close()
        else:
            f = open(txt_path, 'w')
            f.write(data)
            f.close()
    final_data = str(min_seq) + ' ' + str(min_ave) + ' ' + \
                 str(w1) + ' ' + str(w2) + ' ' + str(b1) + ' ' + \
                 str(w3) + ' ' + str(w4) + ' ' + str(b2)
    final_txt_path = '/home/wlw/projects/transfor/force_result/sort/final_28_in_56.txt'
    if os.path.exists(final_txt_path):
        f = open(final_txt_path, 'a')
        f.write(final_data)
    else:
        f = open(final_txt_path, 'w')
        f.write(final_data)
        f.close()
