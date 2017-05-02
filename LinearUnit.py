#coding:utf-8


from Perceptron import Perceptron
import numpy as np
from matplotlib import pyplot as plt

#定义激活函数f
#f = lambda x: x


class LinearUnit(Perceptron):
    def __init__(self, input_num):
        '''初始化线性单元，设置输入参数的个数'''
        Perceptron.__init__(self, input_num, f)


def f(x):
    '''
    定义激活函数f
    '''
    return x


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
    vecspath = '/home/wlw/transfor/pic_coordinator'
    labelpath = '/home/wlw/transfor/x_coordinator'
    input_vecs = get_coordinator(vecspath)
    labels = get_labels(labelpath)
    print input_vecs
    print labels
    #input_vecs = [[459,260], [588,262], [727,265], [890,268], [1050,274], [1218,282], [1388,293]]
    # 期望的输出列表，空间坐标，注意要与输入一一对应
    #labels = [0, 60, 120, 180, 240, 300, 360]
    return input_vecs, labels


def train_linear_unit():
    '''
    使用数据训练线性单元
    '''
    # 创建感知器，输入参数的特征数为1（工作年限）
    lu = LinearUnit(2)
    # 训练，迭代10轮, 学习速率为0.1
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 100, 0.00000001)
    #100000, 0.000001
    #1000000, 0.000001
    #返回训练好的线性单元
    return lu


if __name__ == '__main__':
    '''训练线性单元'''
    linear_unit = train_linear_unit()
    # 打印训练获得的权重
    print 'type: ', type(linear_unit.getvales())
    weights = linear_unit.getvales().split('\t')[0]
    bias = linear_unit.getvales().split('\t')[1]
    weights = float(weights.split(':')[1][1:-1])
    bias = float(bias.split(':')[1])
    print weights
    print bias
    #print linear_unit.split('\t')[1]
    #print linear_unit[1]
    #print linear_unit


    print linear_unit.predict([890, 268])
    print linear_unit.predict([835, 316])
    print linear_unit.predict([772, 372])
    print linear_unit.predict([698, 436])
    print linear_unit.predict([614, 511])
    print linear_unit.predict([515, 598])
    print linear_unit.predict([398, 707])



'''
    # 测试
    print 'Work 3.4 years, monthly salary = %.2f' % linear_unit.predict([3.4])
    print 'Work 15 years, monthly salary = %.2f' % linear_unit.predict([15])
    print 'Work 1.5 years, monthly salary = %.2f' % linear_unit.predict([1.5])
    print 'Work 6.3 years, monthly salary = %.2f' % linear_unit.predict([6.3])
'''

'''
    x = [[5], [3], [8], [1.4], [10.1]]
    #[5], [3], [8], [1.4], [10.1], [3.4], [15], [1.5], [6.3]
    y = [[5500], [2300], [7600], [1800], [11400]]
    #[5500], [2300], [7600], [1800], [11400], [linear_unit.predict([3.4])], [linear_unit.predict([15])], [linear_unit.predict([1.5])], [linear_unit.predict([6.3])]]
    y1 = np.dot(x, weights)+bias
    plt.scatter(x,y,color='blue',label=u'原始数据')
    plt.plot(x,y1,color='k',linewidth='2',label=u'线性回归拟合直线')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(u'梯度下降法求解线性回归')
    plt.show()
'''