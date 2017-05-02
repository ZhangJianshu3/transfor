import os
from matplotlib import font_manager
import matplotlib.pyplot as plt

def read(txtpath):
    file = open(txtpath)
    lines = file.readlines()
    arr = [[] for i in range(len(lines))]
    for i in range(len(lines)):
        lines[i] = lines[i].replace(",", "")
        lines[i] = lines[i].replace("[", "")
        lines[i] = lines[i].replace("]", "")
        lines[i] = lines[i].split(' ')
        #print lines[i]
        for j in lines[i]:
            arr[i].append(float(j))
    return arr


def draw_e(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i], linewidth = '2', label = "e", color='black', linestyle='-', marker='.')

def draw_r(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i], linewidth = '2', label = "e", color='black', linestyle='--', marker='.')


def main(path):
    etxtpath = path+'result.txt'
    #rtxtpath =
    earr = read(etxtpath)
    #rarr =
    print earr
    print len(earr)
    ex = [[] for k in range(len(earr))]
    ey = [[] for k in range(len(earr))]
    for i in range(len(earr)):
        print earr[i]
        for j in range(len(earr[i])):
            if j%2 == 0:
                print earr[i][j], earr[i][j+1]
                ex[i].append(earr[i][j])
                ey[i].append(earr[i][j+1])
    print ex
    print ey
    draw_e(ex, ey)
    #draw_r(rx, ry)





if __name__ == '__main__':
    path = '/home/zhangjianshu/transfor/pic/1/result/'
    main(path)
    plt.show()