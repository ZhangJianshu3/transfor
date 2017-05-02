#coding:utf-8
import numpy as np
import mpl_toolkits.mplot3d
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


def get_dataset():
    # 读取数据
    # 输入向量列表，每一项是图片中的坐标
    vecspath = '/home/zhangjianshu/transfor/pic_test'
    labelpath = '/home/zhangjianshu/transfor/x_test'
    input_vecs = get_coordinator(vecspath)
    labels = get_labels(labelpath)
    #input_vecs = [[459,260], [588,262], [727,265], [890,268], [1050,274], [1218,282], [1388,293]]
    # 期望的输出列表，空间坐标，注意要与输入一一对应
    #labels = [0, 60, 120, 180, 240, 300, 360]
    return input_vecs, labels

if __name__ == '__main__':
    input_vecs = np.array(get_dataset()[0])
    labels = np.array(get_dataset()[1])
    #print x
    w1 = 0.247318942688
    w2 = 0.147631138991
    b = -50.5199595296
    uu = []
    vv = []
    xr = []
    for i in input_vecs:
        uu.append(i[0])
        vv.append(i[1])
    for i in labels:
        xr.append(i)
    u, v = np.mgrid[0:1920:50j, 0:1080:50j]
    xe = []
    i = 0
    for i in range(0, len(xr)):
        xe.append(w1*uu[i]+w2*vv[i]+b)
    ax = plt.subplot(111, projection = '3d')
    print uu
    print vv
    print xr
    print xe
    ax.scatter(uu, vv, xr, color = 'c')
    ax.scatter(uu, vv, xe, color = 'm', marker = 'x')
    ax.set_xlabel('u')
    ax.set_ylabel('v')
    ax.set_zlabel('x')
    plt.show()
