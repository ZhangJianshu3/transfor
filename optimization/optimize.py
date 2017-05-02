#coding:utf-8
import os
import math
import numpy as np
import matplotlib.pyplot as plt


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
    test_vecspath = '/home/zjs/Projects/transfor/optimization/test/pic_test'
    test_x_labelpath = '/home/zjs/Projects/transfor/optimization/test/x_test'
    test_y_labelpath = '/home/zjs/Projects/transfor/optimization/test/y_test'
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

    #拟合q1
    q1_vecspath = '/home/zjs/Projects/transfor/optimization/pic_coord/q1'
    q1_x_labelpath = '/home/zjs/Projects/transfor/optimization/x_coord/q1'
    q1_y_labelpath = '/home/zjs/Projects/transfor/optimization/y_coord/q1'
    q1_vecs_train = np.array(get_dataset(q1_vecspath, q1_x_labelpath, q1_y_labelpath)[0])
    q1_x_train = np.array(get_dataset(q1_vecspath, q1_x_labelpath, q1_y_labelpath)[1])
    q1_y_train = np.array(get_dataset(q1_vecspath, q1_x_labelpath, q1_y_labelpath)[2])
    print 'q1_input_vecs:', q1_vecs_train
    print 'q1_x_labels:', q1_x_train
    print 'q1_y_labels:', q1_y_train
    # 读取像素坐标（u，v）、标记数据xr、yr
    q1_A1 = np.column_stack([q1_vecs_train, np.ones(len(q1_vecs_train))])
    q1_w1, q1_w2, q1_b1 = np.linalg.lstsq(q1_A1, q1_x_train)[0]
    print 'q1_w1:', q1_w1, 'q1_w2:', q1_w2, 'q1_b1:', q1_b1
    q1_A2 = np.column_stack([q1_vecs_train, np.ones(len(q1_vecs_train))])
    q1_w3, q1_w4, q1_b2 = np.linalg.lstsq(q1_A2, q1_y_train)[0]
    print 'q1_w3:', q1_w3, 'q1_w4:', q1_w4, 'q1_b2:', q1_b2

    #拟合q2
    q2_vecspath = '/home/zjs/Projects/transfor/optimization/pic_coord/q2'
    q2_x_labelpath = '/home/zjs/Projects/transfor/optimization/x_coord/q2'
    q2_y_labelpath = '/home/zjs/Projects/transfor/optimization/y_coord/q2'
    q2_vecs_train = np.array(get_dataset(q2_vecspath, q2_x_labelpath, q2_y_labelpath)[0])
    q2_x_train = np.array(get_dataset(q2_vecspath, q2_x_labelpath, q2_y_labelpath)[1])
    q2_y_train = np.array(get_dataset(q2_vecspath, q2_x_labelpath, q2_y_labelpath)[2])
    print 'q2_input_vecs:', q2_vecs_train
    print 'q2_x_labels:', q2_x_train
    print 'q2_y_labels:', q2_y_train
    # 读取像素坐标（u，v）、标记数据xr、yr
    q2_A1 = np.column_stack([q2_vecs_train, np.ones(len(q2_vecs_train))])
    q2_w1, q2_w2, q2_b1 = np.linalg.lstsq(q2_A1, q2_x_train)[0]
    print 'q2_w1:', q2_w1, 'q2_w2:', q2_w2, 'q2_b1:', q2_b1
    q2_A2 = np.column_stack([q2_vecs_train, np.ones(len(q2_vecs_train))])
    q2_w3, q2_w4, q2_b2 = np.linalg.lstsq(q2_A2, q2_y_train)[0]
    print 'q2_w3:', q2_w3, 'q2_w4:', q2_w4, 'q2_b2:', q2_b2

    #拟合q3
    q3_vecspath = '/home/zjs/Projects/transfor/optimization/pic_coord/q3'
    q3_x_labelpath = '/home/zjs/Projects/transfor/optimization/x_coord/q3'
    q3_y_labelpath = '/home/zjs/Projects/transfor/optimization/y_coord/q3'
    q3_vecs_train = np.array(get_dataset(q3_vecspath, q3_x_labelpath, q3_y_labelpath)[0])
    q3_x_train = np.array(get_dataset(q3_vecspath, q3_x_labelpath, q3_y_labelpath)[1])
    q3_y_train = np.array(get_dataset(q3_vecspath, q3_x_labelpath, q3_y_labelpath)[2])
    print 'q3input_vecs:', q3_vecs_train
    print 'q3x_labels:', q3_x_train
    print 'q3y_labels:', q3_y_train
    # 读取像素坐标（u，v）、标记数据xr、yr
    q3_A1 = np.column_stack([q3_vecs_train, np.ones(len(q3_vecs_train))])
    q3_w1, q3_w2, q3_b1 = np.linalg.lstsq(q3_A1, q3_x_train)[0]
    print 'q3_w1:', q1_w1, 'q3_w2:', q3_w2, 'q3_b1:', q3_b1
    q3_A2 = np.column_stack([q3_vecs_train, np.ones(len(q3_vecs_train))])
    q3_w3, q3_w4, q3_b2 = np.linalg.lstsq(q3_A2, q3_y_train)[0]
    print 'q3_w3:', q3_w3, 'q3_w4:', q3_w4, 'q3_b2:', q3_b2

    #拟合q4
    q4_vecspath = '/home/zjs/Projects/transfor/optimization/pic_coord/q4'
    q4_x_labelpath = '/home/zjs/Projects/transfor/optimization/x_coord/q4'
    q4_y_labelpath = '/home/zjs/Projects/transfor/optimization/y_coord/q4'
    q4_vecs_train = np.array(get_dataset(q4_vecspath, q4_x_labelpath, q4_y_labelpath)[0])
    q4_x_train = np.array(get_dataset(q4_vecspath, q4_x_labelpath, q4_y_labelpath)[1])
    q4_y_train = np.array(get_dataset(q4_vecspath, q4_x_labelpath, q4_y_labelpath)[2])
    print 'q4_input_vecs:', q4_vecs_train
    print 'q4_x_labels:', q4_x_train
    print 'q4_y_labels:', q4_y_train
    # 读取像素坐标（u，v）、标记数据xr、yr
    q4_A1 = np.column_stack([q4_vecs_train, np.ones(len(q4_vecs_train))])
    q4_w1, q4_w2, q4_b1 = np.linalg.lstsq(q4_A1, q4_x_train)[0]
    print 'q4_w1:', q4_w1, 'q4_w2:', q4_w2, 'q4_b1:', q4_b1
    q4_A2 = np.column_stack([q4_vecs_train, np.ones(len(q4_vecs_train))])
    q4_w3, q4_w4, q4_b2 = np.linalg.lstsq(q4_A2, q4_y_train)[0]
    print 'q4_w3:', q4_w3, 'q4_w4:', q4_w4, 'q4_b2:', q4_b2

    #拟合center
    center_vecspath = '/home/zjs/Projects/transfor/optimization/pic_coord/center'
    center_x_labelpath = '/home/zjs/Projects/transfor/optimization/x_coord/center'
    center_y_labelpath = '/home/zjs/Projects/transfor/optimization/y_coord/center'
    center_vecs_train = np.array(get_dataset(center_vecspath, center_x_labelpath, center_y_labelpath)[0])
    center_x_train = np.array(get_dataset(center_vecspath, center_x_labelpath, center_y_labelpath)[1])
    center_y_train = np.array(get_dataset(center_vecspath, center_x_labelpath, center_y_labelpath)[2])
    print 'center_input_vecs:', center_vecs_train
    print 'center_x_labels:', center_x_train
    print 'center_y_labels:', center_y_train
    # 读取像素坐标（u，v）、标记数据xr、yr
    center_A1 = np.column_stack([center_vecs_train, np.ones(len(center_vecs_train))])
    center_w1, center_w2, center_b1 = np.linalg.lstsq(center_A1, center_x_train)[0]
    print 'center_w1:', center_w1, 'center_w2:', center_w2, 'center_b1:', center_b1
    center_A2 = np.column_stack([center_vecs_train, np.ones(len(center_vecs_train))])
    center_w3, center_w4, center_b2 = np.linalg.lstsq(center_A2, center_y_train)[0]
    print 'center_w3:', center_w3, 'center_w4:', center_w4, 'center_b2:', center_b2


    # 求坐标的估计值
    xe = []
    ye = []
    i = 0
    for i in range(0, len(u)):
        print u[i],v[i]
        if 698<u[i]<1259 and 436<v[i]<663:
            print 'center'
            xe.append(center_w1 * u[i] + center_w2 * v[i] + center_b1)
            ye.append(center_w3 * u[i] + center_w4 * v[i] + center_b2)
        elif u[i]<1000 and v[i]<490:
            print 'q1'
            xe.append(q1_w1 * u[i] + q1_w2 * v[i] + q1_b1)
            ye.append(q1_w3 * u[i] + q1_w4 * v[i] + q1_b2)
        elif u[i]>1000 and v[i]<490:
            print 'q2'
            xe.append(q2_w1 * u[i] + q2_w2 * v[i] + q2_b1)
            ye.append(q2_w3 * u[i] + q2_w4 * v[i] + q2_b2)
        elif u[i]<1000 and v[i]>490:
            print 'q3'
            xe.append(q3_w1 * u[i] + q3_w2 * v[i] + q3_b1)
            ye.append(q3_w3 * u[i] + q3_w4 * v[i] + q3_b2)
        elif u[i]>1000 and v[i]>490:
            print 'q4'
            xe.append(q4_w1 * u[i] + q4_w2 * v[i] + q4_b1)
            ye.append(q4_w3 * u[i] + q4_w4 * v[i] + q4_b2)

    ax = plt.subplot(111)
    ax.scatter(xr, yr, color='c')
    ax.scatter(xe, ye, color='m', marker='x')
    plt.show()
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
    print 'max:', max
    print 'min:', min
    print 'ave:', ave
'''
    # 将每次的结果写入txt
    data = 'optimization' + ' ' + \
           str(ave) + ' ' + str(max) + ' ' + str(min) + '\n'

    txt_path = '/home/zjs/Projects/transfor/optimization/result.txt'
    if os.path.exists(txt_path):
        f = open(txt_path, 'a')
        f.write(data)
        f.close()
    else:
        f = open(txt_path, 'w')
        f.write(data)
        f.close()
'''