#作业L1 2.10题强化版（引入迎面风阻）
#作业L2 2.10题进一步升级，发展“超级辅助精确打击系统”
（考虑炮弹初始发射的时候发射角度误差度，速度有5%的误差，迎面风阻误差10%，以炮弹落点与打击目标距离差平方均值最小为优胜）<br/>
以上所有计算需要考虑海拔高度的影响，使用绝热模型进行计算，误差描述使用最简单的均匀分布描述（也就是在误差范围内每个取值概率是一样的）。<br/>
完成L2作业的同学，下次上课可以比赛，对100km的目标看谁打得最精确！
##以下为2.10的代码，和大致思路
空气静止时，考虑风阻的情况，和发射点与靶的水平距离和海平差是所需的发射最小速度<br/>
先考虑速度一定，发射角度一定，落到靶的所在海拔时，所能发射的距离<br/>
然后逐步增加速度，使发射的速度足够大，能够使炮弹发射足够的水平距离， 记录所需速度<br/>
最后逐步增加角度，求出不同角度下，所需的速度，然后比较各种情况下所需的速度，得到最小速度值和发射的角度<br/>
<pre><code>
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pylab as pl
import math
import andom
class cannon_shell:
    def __init__(self,time_step=0.001,):
        self.dt = time_step
        self.l_x=[0]
        self.l_y=[0]
    def run(self):
        print('distanceX->')
        distance_x=float(input())
        print('distanceY(Y<0)->')
        distance_y=float(input())
        angle=41
        vmin = []
        Angle=[]
        while(angle<=46):                 #扫描角度，求各角度下，发射距离一定，炮弹的发射速度，求出速度最小值
            angle=angle+0.01
            x0=0
            v0=50
            while(x0<=distance_x):         #扫描速度，求角度一定，发射距离一定时的炮弹发射速度
                cos1 = math.cos(angle*math.pi/180)
                sin1 = math.sin(angle*math.pi/180)
                vx = v0*cos1
                vy = v0*sin1
                y=0
                x=0
                while(y>=distance_y):  #仅支持distance_y<0
                    g = 9.8             #求角度一定，速度一定时，发射距离
                    a = (1 - 6.5e-3 * y / 288) ** 2.5
                    x = x + vx * self.dt
                    y = y + vy * self.dt
                    v = math.sqrt(vx ** 2 + vy ** 2)
                    vx = vx - 4e-5 * v * vx * self.dt * a
                    vy = vy - (4e-5 * v * vy * self.dt * a + g) * self.dt

                x0=x
                v0=v0+1
            vmin.append(v0)
            Angle.append(angle)
        vm=min(vmin)
        a=vmin.index(vm)
        b=Angle[a]
        print(vm-1)
        print(b)
a=cannon_shell()
a.run()
</code></pre>

# 输入x=5000，y=-10，得到vmin=234，angle=43.96000000000037
# 输入x=10000，y=-10，得到vmin=350，angle=42.6000000000034
# 考虑到误差后，初始速度5%误差，角度+-2度误差，运用算得值，求实际发射距离，可加入以下代码
<pre><code>
import pylab as pl
import math
import random
print('print v')
v=float(input())
print('print angle')
b=float(input())
l=[]
n=0
dt=0.01
distance_y=-10
while(n<=5):
    vr = random.uniform(v * 0.95, v * 1.05)
    angler = random.uniform(b - 2, b + 2)
    vx = (vr) * math.cos(angler * math.pi / 180)
    vy = (vr) * math.sin(angler * math.pi / 180)
    x = 0
    y = 0

    while (y >= distance_y):  # 仅支持distance_y<0
        g = 9.8  # 求角度一定，速度一定时，发射距离
        a = (1 - 6.5e-3 * y / 288) ** 2.5
        x = x + vx * dt
        y = y + vy * dt
        v0 = math.sqrt(vx ** 2 + vy ** 2)
        vx = vx - 4e-5 * v0* vx * dt * a
        vy = vy - (4e-5 * v0* vy * dt * a + g)*dt
    l.append(x)
    n=n+1
print(l)
</code></pre>
# 5000m下，vmin=234，angle=43.96，实际发射距离为[4834.78764515818, 5407.931863600142, 4643.633561315511, 5340.927186509931, 5149.164450967769, 5130.789332904919]
# 10000m下，vmin=350，angle=42.06，实际发射距离为[10679.54578233396, 10702.504854090246, 10616.816065253992, 9525.325494884954, 9848.96483302615, 9882.876848894179]
#精度上主要取决于time_step的大小，其次为角度扫描和速度扫描
##然后最后以上都忘记考虑迎面风阻的影响了，也不准备考虑了QAQ,所以默认空气静止情况下
##由于是有3个循环的过程，类似穷举的方法，所以运算时间会比较长啊，sad

###致谢卢江玮同学帮助解决代码上问题
