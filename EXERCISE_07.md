# Excercise_07
***

#### Exercise 3.12
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the drive force; that 
is, at times <img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn.gif?raw=true" alt="" title="" />,
where <img src="http://latex.codecogs.com/gif.latex?n" alt="" title="" /> is an integer. At these values of
<img src="http://latex.codecogs.com/gif.latex?t" alt="" title="" /> the driving force passed through zero [see(3.18)]. 
However, we could jusi as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times
<img src="http://latex.codecogs.com/gif.latex?\pi/4" alt="" title="" /> out-of-phase with this force, etc. Construct the Poincaré
sections for these cases and compare them with Figure 3.9.

#### Exercise 3.13
Write a program to calculate and compare the behavior of two, nearly identical pendulums. Use it to calculate the divergence of two
nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent
from the slope of a plot of <img src="http://latex.codecogs.com/gif.latex?log(\Delta\theta)" alt="" title="" /> as a function of 
<img src="http://latex.codecogs.com/gif.latex?t" alt="" title="" />.

#### Exercise 3.14
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent
compare with that found in Figure 3.7?

###1. 理论推导
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;过去我们已经学习了一些单摆的基础知识，在无阻尼和驱动力且摆角很小的情况下单摆的动力学方程近似为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(1).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;显然， 这种情况下单摆近似地做简谐运动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(3).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果我们考虑阻尼，单摆的动力学方程会变为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(2).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这时，单摆将会做阻尼振动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(4).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时单摆将做振幅逐渐减小的周期性阻尼振动，经过较长时间后，振幅几乎为零，可以认为振动停止。然而，如果有驱动力，情况又将大不一样，单摆的运动学方程变为

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(5).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这时单摆做受迫振动，有

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(6).gif?raw=true" alt="" title="" />
</div>
其中<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(7).gif?raw=true" alt="" title="" />
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;然而，在摆角较大时，近似<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(8).gif?raw=true" alt="" title="" />不再成立，我们必须设法求解如下非线性方程

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(9).gif?raw=true" alt="" title="" />
</div>

###2.算法探讨
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们如果依然采用欧拉法，将得到发散的解，显然这与实际不符，在此我们采用欧拉-克罗默方法求数值解，步骤如下

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(10).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(11).gif?raw=true" alt="" title="" />
</div>

<div align=center>
<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(12).gif?raw=true" alt="" title="" />
</div>

注意，若<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(13).gif?raw=true" alt="" title="" />不在区间<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(14).gif?raw=true" alt="" title="" />内，我们须通过加或减<img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Excercise_07/CodeCogsEqn%20(15).gif?raw=true" alt="" title="" />使其落入区间内。

##代码如下所示
<pre><code>
import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=2/3

'''
print('The l ->')
l=float(input())
print('The q ->')
q=float(input())
print('The ou_d ->')
ou_d=float(input())
print('F_D->')
F_D=float(input())
print('theta->')
theta=float(input())
'''

class pendulum:
    def __init__(self,F_D,theta):
        self.theta=[theta]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def run(self):

        while self.t[-1]<60:
            omiga_new=self.omiga[-1]-((g/l)*mt.sin(self.theta[-1])+q*self.omiga[-1]-self.F_D*mt.sin(ou_d*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            theta_new=(self.theta[-1]+self.omiga[-1]*self.dt)
            if theta_new>mt.pi:
                theta_new=theta_new-2*mt.pi
            if theta_new<-(mt.pi):
                theta_new=theta_new+2*mt.pi
            self.theta.append(theta_new)
            t_new=self.t[-1]+self.dt
            self.t.append(t_new)



sub1=pl.subplot(251)
A=pendulum(0,0.2)
A.run()
sub1.plot(A.t,A.theta,'g',label='$F_D=0$')
sub1.set_title('$θ$ versus time')
sub1.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub2=pl.subplot(252)
A=pendulum(0.5,0.2)
A.run()
sub2.plot(A.t,A.theta,'g',label='$F_D=0.5$')
sub2.set_title('$θ$ versus time')
sub2.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub3=pl.subplot(253)
A=pendulum(1.0,0.2)
A.run()
sub3.plot(A.t,A.theta,'g',label='$F_D=1.0$')
sub3.set_title('$θ$ versus time')
sub3.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub4=pl.subplot(254)
A=pendulum(1.5,0.2)
A.run()
sub4.plot(A.t,A.theta,'g',label='$F_D=1.5$')
sub4.set_title('$θ$ versus time')
sub4.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub5=pl.subplot(255)
A=pendulum(2.0,0.2)
A.run()
sub5.plot(A.t,A.theta,'g',label='$F_D=2.0$')
sub5.set_title('$θ$ versus time')
sub5.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub6=pl.subplot(256)
A=pendulum(0,0.2)
A.run()
sub6.plot(A.t,A.omiga,'b',label='$F_D=0$')
sub6.set_title('$θ$ versus time')
sub6.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub7=pl.subplot(257)
A=pendulum(0.5,0.2)
A.run()
sub7.plot(A.t,A.omiga,'b',label='$F_D=0.5$')
sub7.set_title('$θ$ versus time')
sub7.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub8=pl.subplot(258)
A=pendulum(1.0,0.2)
A.run()
sub8.plot(A.t,A.omiga,'b',label='$F_D=1.0$')
sub8.set_title('$θ$ versus time')
sub8.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub9=pl.subplot(259)
A=pendulum(1.5,0.2)
A.run()
sub9.plot(A.t,A.omiga,'b',label='$F_D=1.5$')
sub9.set_title('$θ$ versus time')
sub9.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

sub10=pl.subplot(2,5,10)
A=pendulum(2.0,0.2)
A.run()
sub10.plot(A.t,A.omiga,'b',label='$F_D=2.0$')
sub10.set_title('$θ$ versus time')
sub10.legend(loc="upper right",frameon=False)
pl.ylabel('$θ$(radians)')
pl.xlabel('time(s)')

pl.show()
</code></pre>

# 得到图像如下所示
![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1-2.png)

#下面考虑3.12题
##先考虑在一般情况下任意时间的图像，代码如下
<pre><code>
import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=2/3
class pendulum:
    def __init__(self,F_D,theta):
        self.theta=[theta]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.04
        self.F_D=F_D
    def run(self):
        while self.t[-1]<60:
            omiga_new=self.omiga[-1]-((g/l)*mt.sin(self.theta[-1])+q*self.omiga[-1]-self.F_D*mt.sin(ou_d*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            theta_new=(self.theta[-1]+self.omiga[-1]*self.dt)
            if theta_new>mt.pi:
                theta_new=theta_new-2*mt.pi
            if theta_new<-(mt.pi):
                theta_new=theta_new+2*mt.pi
            self.theta.append(theta_new)
            t_new=self.t[-1]+self.dt
            self.t.append(t_new)


pl.subplot(121)
A = pendulum(0.5, 0.2)
A.run()
pl.plot(A.theta, A.omiga, 'r.', label='$F_D=0.5$')
pl.title('$ω$ versus $θ$')
pl.legend(loc="upper right", frameon=False)
pl.xlabel('$θ$(radians)')
pl.ylabel('$ω$(radians/s)')

pl.subplot(122)
A = pendulum(1.2, 0.2)
A.run()
pl.plot(A.theta, A.omiga, 'r.', label='$F_D=1.2$')
pl.title('$ω$ versus $θ$')
pl.legend(loc="upper right", frameon=False)
pl.xlabel('$θ$(radians)')
pl.ylabel('$ω$(radians/s)')

pl.show()
</code></pre>
##得到图像如图所示
![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1-4.png)
##当FD=0.5时，庞加莱界面上大致是一封闭曲线，可以认为运动是准周期的;而当FD=1.2时，庞加莱截面上是一些成片的具有分形结构的密集点，运动变为混沌的
##考虑在特定的时间点附近的omega和theta的分布情况，代码如下
<pre><code>
import pylab as pl
import math  as mt
g=9.8
l=9.8
q=0.5
ou_d=float(2/3)


class pendulum:
    def __init__(self,F_D,theta):
        self.theta=[theta]
        self.omiga=[0]
        self.t=[0]
        self.dt=0.01
        self.F_D=F_D
        self.omiga_need=[0]
        self.theta_need=[0]
    def run(self):

        while self.t[-1]<5000:
            omiga_new=self.omiga[-1]-((g/l)*mt.sin(self.theta[-1])+q*self.omiga[-1]-self.F_D*mt.sin(ou_d*self.t[-1]))*self.dt
            self.omiga.append(omiga_new)
            theta_new=(self.theta[-1]+self.omiga[-1]*self.dt)
            if theta_new>mt.pi:
                theta_new=theta_new-2*mt.pi
            if theta_new<-(mt.pi):
                theta_new=theta_new+2*mt.pi
            self.theta.append(theta_new)
            t_new=self.t[-1]+self.dt
            self.t.append(t_new)

        a=len(self.theta)

        for i in range(a):
            if (self.t[i]*ou_d)%(2*mt.pi)<0.01 :
                self.theta_need.append(self.theta[i])
                self.omiga_need.append(self.omiga[i])
            elif abs(self.t[i]-mt.pi/4)<0.01:
                self.theta_need.append(self.theta[i])
                self.omiga_need.append(self.omiga[i])

    def draw(self):
        pl.plot(self.theta_need, self.omiga_need, 'r.')
        pl.title('$θ$ versus time')
        pl.legend(loc="upper right", frameon=False)
        pl.ylabel(r'$\omega$(radians/s)')
        pl.xlabel(r'$\theta$[randians]')
        pl.show()
A1=pendulum(1.2,0.2)
A1.run()
A1.draw()

</code></pre>
#得到下图图像
![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1-3.png)
###我们可以观察到奇异 吸引子
###心得，混沌并非等同于复杂，混沌现象普遍存在于大量非线性系统中，结构简单如单摆也可能做混沌运动；存在混沌现象动力学系统对初值十分敏感，简单原因可导致复杂后果；混沌理论与分形几何学有着密不可分的联系，后者是研究前者的有力工具。

##致谢倪世杰同学的代码帮助

