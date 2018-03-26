import math
import numpy as np

# Runge-Kutta Method for Systems of Differential Equations
def RungeKuttaSystem(funclist,a,b,n,alphalist,realfunc=None):
	assert len(funclist)==len(alphalist)

	m=len(alphalist)
	h=(b-a)/n
	t=a
	wlist=np.copy(alphalist)
	k=np.zeros([4,m])

	if realfunc is not None:
		for j in range(m):
			print ("t0: %f, u%d(t): %f, exact: %f, error: %f"%(t,j,wlist[j],realfunc[j](t),abs(realfunc[j](t)-wlist[j])))
	else:
		for j in range(m):
			print ("t0: %f, u%d(t): %f"%(t,j,wlist[j]))
	
	for i in range(1,n+1):
		for j in range(m):	
			k[0,j] = h*funclist[j](t,wlist)
		for j in range(m):
			k[1,j] = h*funclist[j](t+h/2,wlist+0.5*k[0,:])
		for j in range(m):
			k[2,j] = h*funclist[j](t+h/2,wlist+0.5*k[1,:])
		for j in range(m):
			k[3,j] = h*funclist[j](t+h,wlist+k[2,:])
		for j in range(m):
			wlist[j]= wlist[j] + (k[0,j] + 2*k[1,j] + 2*k[2,j] + k[3,j])/6
		t=a+i*h
		if realfunc is not None:
			for j in range(m):
				print ("t%d: %f, u%d(t%d): %f, exact: %f, error: %f"%(i,t,j,i,wlist[j],realfunc[j](t),abs(realfunc[j](t)-wlist[j])))
		else:
			for j in range(m):
				print ("t%d: %f, u%d(t): %f"%(i,t,j,wlist[j]))

if __name__== "__main__":
	# def func1(t,ylist):
	# 	u1=ylist[0]
	# 	u2=ylist[1]
	# 	return -4*u1 + 3*u2 + 6
	# def func2(t,ylist):
	# 	u1=ylist[0]
	# 	u2=ylist[1]
	# 	return -2.4*u1 + 1.6*u2 + 3.6
	# funclist1=[func1,func2]
	# alphalist=(0.0,0.0)
	# RungeKuttaSystem(funclist1,0.0,0.5,5,alphalist)

	def func1(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		return 3*u1 + 2*u2 - (2*t**2 + 1)*math.exp(2*t)
	def func2(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		return 4*u1 + u2 + (t**2 + 2*t - 4)*math.exp(2*t)
	funclist1=[func1,func2]

	def func1(t):
		return math.exp(5*t)/3-math.exp(-t)/3+math.exp(2*t)
	def func2(t):
		return math.exp(5*t)/3+2*math.exp(-t)/3+t**2*math.exp(2*t)
	realfunclist1=[func1,func2]

	alphalist=(1.0,1.0)
	RungeKuttaSystem(funclist1,0.0,1.0,5,alphalist,realfunc=realfunclist1)

	def func1(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		u3=ylist[2]
		return u2
	def func2(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		u3=ylist[2]
		return -u1-2*math.exp(t)+1
	def func3(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		u3=ylist[2]
		return -u1-math.exp(t)+1
	funclist1=[func1,func2,func3]

	def func1(t):
		return math.cos(t)+math.sin(t)-math.exp(t)+1
	def func2(t):
		return math.cos(t)-math.sin(t)-math.exp(t)
	def func3(t):
		return math.cos(t)-math.sin(t)
	realfunclist1=[func1,func2,func3]

	alphalist=(1.0,0.0,1.0)
	RungeKuttaSystem(funclist1,0.0,2,4,alphalist,realfunc=realfunclist1)


	def func1(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		return u2
	def func2(t,ylist):
		u1=ylist[0]
		u2=ylist[1]
		return 2/t*u2-2/t**2*u1+t*math.log(t)
	funclist1=[func1,func2]

	def func1(t):
		return 7.0/4*t+0.5*t**3*math.log(t)-3*t**3/4
	def func2(t):
		return 7.0/4+0.5*t**2+1.5*t**2*math.log(t)-9*t**2/4
	realfunclist1=[func1,func2]

	alphalist=(1.0,0.0)
	RungeKuttaSystem(funclist1,1.0,2.0,10,alphalist,realfunc=realfunclist1)
