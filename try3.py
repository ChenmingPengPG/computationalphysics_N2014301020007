import matplotlib.pyplot as pl
import numpy as np
import math
import random
class particle(object):#def a class"particle"
	diret = 0
	def __init__(self,x,y,state):
		self.x=x
		self.y=y
		self.state=state
	def moveparticle(self):
		if self.diret==0:
			self.x=self.x+0.5
		elif self.diret==1:
			self.x=self.x-0.5
		elif self.diret==2:
			self.y=self.y-0.5
		elif self.diret==3:
			self.y=self.y+0.5
		else :
			print ('error2')
		self.diret=random.randint(0,3)
		return
class screen(object):#def a class"screen"
	lis=[particle(50.0,50.0,0)]
	state=1
	def chargepoint(self,x,y):
		for i in self.lis:
			if i.x==x and i.y==y:
				return 1
		return 0
	def addparticle(self,x=65.0,y=65.0):#add a new particle
		i=self.chargepoint(x,y)
		if self.state==1:
			if i==0:
				self.lis.append(particle(x,y,1))
			else:
				print ('same particle')
				self.state=0
		else:
			print ('full screen')
		for a in self.lis:
			if a.x>66.0 or a.y>66.0 or a.x<34.0 or a.y<34.0:
				self.state=0
		return
	def delparticle(self,x,y):
		for i in range(len(self.lis)):
			if self.lis[i].x==x and self.lis[i]==y:
				self.lis.pop(i)
				self.state=1
				return
		return
	def showscreen(self):
		x=[]
		y=[]
		for i in self.lis:
			x.append(i.x)
			y.append(i.y)
		pl.plot(x,y,'.')
		pl.show()
	def move(self):#random walk of particle
		t1=self.lis.pop()
		while t1.state==1 and t1.x<75.0 and t1.y<75.0 and t1.x>=25 and t1.y>=25:
			i1=self.chargepoint(t1.x+0.5,t1.y)
			i2=self.chargepoint(t1.x-0.5,t1.y)
			i3=self.chargepoint(t1.x,t1.y-0.5)
			i4=self.chargepoint(t1.x,t1.y+0.5)
			s=[i1,i2,i3,i4]
			if i1==0 and i2==0 and i3==0 and i4==0:
				t1.moveparticle()
			elif random.randint(1,100)>85:
				t1.state=0
			elif i1==1 and i2==1 and i3==1 and i4==1:
				t1.state=0
			else:
				while s[t1.diret]==1:
					t1.diret=random.randint(0,3)
				t1.moveparticle()
			#print 'move a particle'
			#print t1.x,t1.y
		if t1.state==0 :
			self.lis.append(t1)
if __name__=='__main__':
	sc=screen()
	n=0
	while sc.state==1:
		i=random.randint(70,130)
		x=i/2.0
		r=(15**2-(x-50)**2)**0.5#The new particle can appear where r = 15
		k=int(r*2)
		y1=k/2.0
		if random.randint(1,2)==1:
			y=50+y1
		else:
			y=50-y1
		print (x,y)
		sc.addparticle(x,y)
		print ('generate a new particle')
		print (len(sc.lis),sc.state)
		#s=raw_input(':')
		sc.move()
	print (len(sc.lis))
	sc.showscreen()

