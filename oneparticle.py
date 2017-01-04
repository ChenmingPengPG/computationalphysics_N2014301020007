# -*- coding:utf-8 -*-
import pylab as pl
import numpy as np
import math
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation

class oneparticle():
    def __init__(self,x0=0,dt=0.1,T=10,p1=0.5,p2=0.6,x2ave=0):
        self.x1=[x0]
        self.t1=[0]
        self.x2 = [x0]
        self.t2 = [0]
        self.T=T
        self.dt=dt
        self.y=[0]
        self.num=[0]
        self.num1=[0]
        self.num2 = [0]
        self.p1=p1
        self.p2=p2
        self.x2ave=[x2ave]
        self.x=[0]
        self.y=[0]
    def run(self):
        x2ave=0
        xnew1=0
        xnew2=0
        for i in range (1,100):
            xnew=0
            for j in range (i):
                if (random.random()<0.5):
                    dx=-1
                else:
                    dx=1
                xnew=xnew+dx
            x2ave=x2ave+xnew**2
            xx=x2ave/i
            self.x.append(xx)
            self.num.append(self.num[-1]+1)
        for i in range (100):
            if (random.random() < 0.5):
                dx = -1
            else:
                dx = 1
            xnew1=xnew1+dx
            self.x1.append(xnew1)
            self.num1.append(self.num1[-1]+1)
            self.y.append(0)
        for i in range(100):
            if (random.random() < 0.5):
                dx = -1
            else:
                dx = 1
            xnew2 = xnew2 + dx
            self.x2.append(xnew2)
            self.num2.append(self.num2[-1] + 1)
        #print(self.num,self.x)
    def show(self):
        pl.subplot(122)
        pl.plot(self.num, self.x, 'bo', label='$<x^2>$versus time,n=100')
        pl.xlabel('step number')
        pl.ylabel('$<x^2>$')
        pl.title('Random walk in one dimension')
        pl.xlim(0, 100)
        pl.ylim(0, 100)
        pl.axis('equal')
        pl.legend(loc='upper left', frameon=False)

        pl.subplot(121)
        pl.plot(self.num1, self.x1, 'bo', label='walker1')
        pl.plot(self.num2, self.x2, 'ro', label='walker2')
        pl.xlabel('step number')
        pl.ylabel('x')
        pl.xlim(0,100)
        pl.ylim(-20.20)
        pl.axis('equal')
        pl.legend(loc='best',frameon=False)

        pl.show()
    def show_trajectory(self):
        fig = plt.figure()
        ax = plt.axes(title=('Random Walk'),
                      aspect='equal', autoscale_on=False,
                      xlim=(-1.1, 1.1), ylim=(-1.1, 1.1),
                      xlabel=('x'), ylabel=('y'))
        line = ax.plot([], [], 'b')
        point = ax.plot([], [], 'ro', markersize=10)
        images = []


        def init():
            line = ax.plot([], [], 'b', markersize=8)
            point = ax.plot([], [], 'ro', markersize=10)
            return line, point

        def anmi(i):
            ax.clear()
            line = ax.plot(self.x1[0:(1 * i)], self.y[0:(1 * i)], 'b', markersize=8)
            point = ax.plot(self.x1[(1 * i - 1):(1* i)], self.y[(1 * i - 1):(1 * i)], 'ro', markersize=10)
            return line, point

        anmi = animation.FuncAnimation(fig, anmi, init_func=init, frames=1000, interval=1,
                                       blit=False)
        plt.show()
a=oneparticle()
a.run()
a.show()
a.show_trajectory()


