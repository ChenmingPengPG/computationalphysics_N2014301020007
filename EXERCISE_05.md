# Problem 2.9
 Calculate the trajectory of our cannon shell including both air drag and the reduced air density at high altitudes so that you <br/> 
 can reproduce the results in Figure 2.5.Perform your calculation for different firing angles ande determine the value of the angle that gives the maximum range.<br/>

## 由书本分析得到
![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%5CDelta%20t) <br/>
![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t)<br/>
![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci%7D%5CDelta%20t)<br/>
![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t)<br/>



##  结合以上所述，以下是得到的代码
<pre><code>
import pylab as pl
import math
class cannon_shell:
    def __init__(self,power=10,mass=1,time_step=0.1,total_time=20,initial_velocity=700,x0=0,y0=0,):
        self.v = initial_velocity
        self.t = 0
        self.m = mass
        self.p = power
        self.dt = time_step
        self.time = total_time
        self.l_x=[x0]
        self.l_y=[y0]
    def run(self):
        _time=0
        print('the launch angel,2,3,4,5' )
        angel1 = int(input())
        cos1 = math.cos(angel1*math.pi/180)
        sin1 = math.sin(angel1*math.pi/180)
        vx = self.v*cos1
        vy = self.v*sin1
        x = 0
        y = 0
        while(y>=0):
            b2_m=4e-5
            g=9.8
            a = (1 - 6.5e-3*y/ 288)**2.5
            x=x+vx*self.dt
            y=y+vy*self.dt
            self.v=math.sqrt(vx**2+vy**2)
            vx=vx-4e-5*self.v*vx*self.dt*a
            vy=vy-(4e-5*self.v*vy*self.dt*a+g)*self.dt
            _time += self.dt
            self.l_x.append(x)
            self.l_y.append(y)
a=cannon_shell()
a.run()
b=cannon_shell()
b.run()
c=cannon_shell()
c.run()
d=cannon_shell()
d.run()
e=cannon_shell()
e.run()
pl.plot(a.l_x,a.l_y,'r')
pl.plot(b.l_x,b.l_y,'g')
pl.plot(c.l_x,c.l_y,'d')
pl.plot(d.l_x,d.l_y,'b')
pl.plot(e.l_x,e.l_y,'c')
font = {'family': 'serif',
                'color': 'darkred',
                'weight': 'normal',
                'size': 16,
                }
pl.title('cannon shell including both air drag and the reduced air density at high altitudes', fontdict=font)
pl.xlabel('x ($m$)')
pl.ylabel('y ($m$)')
pl.ylim(0)
pl.show()
</code></pre>
# 得到的图形如下所示,分别是射击角度在15°,30°,45°,60°,75° 所得到的
![](https://github.com/Damonphysics/computationalphysics_N2014301020007/blob/master/figure_1.png)
  
 
