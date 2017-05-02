#coding:utf-8
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

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


def get_training_dataset():
    # 构建训练数据
    # 输入向量列表，每一项是图片中的坐标
    vecspath = '/home/zjs/Projects/transfor/pic_coordinator'
    labelpath = '/home/zjs/Projects/transfor/x_coordinator'
    input_vecs = get_coordinator(vecspath)
    labels = get_labels(labelpath)
    #input_vecs = [[459,260], [588,262], [727,265], [890,268], [1050,274], [1218,282], [1388,293]]
    # 期望的输出列表，空间坐标，注意要与输入一一对应
    #labels = [0, 60, 120, 180, 240, 300, 360]
    return input_vecs, labels

if __name__ == '__main__':
    input_vecs = np.array(get_training_dataset()[0])
    labels = np.array(get_training_dataset()[1])
    #print x
    A = np.column_stack([input_vecs, np.ones(len(input_vecs))])
    w1, w2, b = np.linalg.lstsq(A, labels)[0]
    print w1, w2, b
    uu = []
    vv = []
    xx = []
    for i in input_vecs:
        uu.append(i[0])
        vv.append(i[1])
    for i in labels:
        xx.append(i)
    print uu
    u, v = np.mgrid[0:1920:50j, 0:1080:50j]
    x = w1*u+w2*v+b
    ax = plt.subplot(111, projection = '3d')
    ax.plot_surface(u, v, x, rstride=5, cstride=5, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha = 0.3)
    ax.scatter(uu, vv, xx, color = 'r')
    ax.set_xlabel('u')
    ax.set_ylabel('v')
    ax.set_zlabel('x')
    plt.show()