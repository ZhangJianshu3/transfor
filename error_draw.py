#coding:utf-8
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




if __name__ == '__main__':
    test_vecspath = '/home/zjs/Projects/transfor/optimization/test/pic_test'
    test_x_labelpath = '/home/zjs/Projects/transfor/optimization/test/x_test'
    test_y_labelpath = '/home/zjs/Projects/transfor/optimization/test/y_test'
    test_input_vecs = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[0])
    test_x_labels = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[1])
    test_y_labels = np.array(get_dataset(test_vecspath, test_x_labelpath, test_y_labelpath)[2])
    w1 = 0.245012487727
    w2 = 0.152769676336
    b1 = -50.4548128135
    w3 = -0.0510113082818
    w4 = 0.596959007094
    b2 = -51.5904181735

    u = []
    v = []
    for i in test_input_vecs:
        u.append(i[0])
        v.append(i[1])

    #实际坐标
    xr = []
    yr = []
    for i in test_x_labels:
        xr.append(i)
    for i in test_y_labels:
        yr.append(i)

    #拟合坐标
    xe = []
    ye = []
    i = 0
    for i in range(0, len(u)):
        xe.append(w1 * u[i] + w2 * v[i] + b1)
        ye.append(w3 * u[i] + w4 * v[i] + b2)

    print 'xr:', xr
    print 'yr:', yr
    print 'xe:', xe
    print 'ye:', ye

    #画图
    ax = plt.subplot(111)
    ax.scatter(xr, yr, color='c')
    ax.scatter(xe, ye, color='m', marker='x')
    plt.show()
