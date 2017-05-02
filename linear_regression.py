# -*- coding:utf-8 -*-
#######################################################################
# 源码为小编原创，对该源码有任何疑问，请在公众号内回复 微店，
# 通过购买答疑券（1元/份）获取解答，更多源码资料请关注公众号djangoSpace
#######################################################################
# 梯度下降算法求解线性回归，python版本：2.7.9
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-2,2,0.1)
y = 2*x+np.random.random(len(x))
x = x.reshape((len(x),1))
y = y.reshape((len(x),1))
# 原始数据
# plt.scatter(x,y);plt.xlabel("x");plt.ylabel("y");plt.title(u'原始数据');plt.grid(True);plt.show()
maxgen = 1000
#1000
# 初始化seta
# seta = np.random.random(3) # 一维向量
seta = np.array([0])
b = 0 # 常数项
alpha0 = 0.001
#0.001
for i in range(maxgen):
    alpha = 1/float(i+1)+alpha0
    e = np.dot(x,seta.reshape((len(seta),1)))+b-y # 二维列向量
    mse = np.linalg.norm(e)
    delta_seta = np.dot(e.T,x)[0]
    delta_seta_norm = np.linalg.norm(delta_seta)
    b = b-alpha*np.sum(e)
    seta = seta-alpha*delta_seta
    print u'迭代次数：',i
    print u'梯度：',delta_seta_norm,'seta',seta,'b:',b,'mse',mse
    print 'alpha:',alpha,'sum(e):',sum(e)


y1 = np.dot(x,seta.reshape((len(seta),1)))+b
plt.scatter(x,y,color='blue',label=u'原始数据')
plt.plot(x,y1,color='k',linewidth='2',label=u'线性回归拟合直线')
#plt.text(0,-0.5,'y='+str(seta[0])+'x+'+str(b))
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'梯度下降法求解线性回归')
#plt.legend()
#plt.grid(True)
plt.show()


