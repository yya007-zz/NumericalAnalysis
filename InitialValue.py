import math
import numpy as np

def Euler(func,a,b,n,alpha,realfunc=None):
	h=(b-a)/n
	t=a
	w=alpha
	if realfunc is not None:
		print ("t0: %f, w0: %f, y0: %f, |y0-w0|: %f"%(t,w,realfunc(t),abs(realfunc(t)-w)))
	else:
		print ("t0: %f, w0: %f"%(t,w))

	value=[]
	res=[]
	value.append(t)
	res.append(w)
	for i in range(1,n+1):
		w+=h*func(w,t)
		t=a+i*h
		if realfunc is not None:
			print ("t%d: %f, w%d: %f, y%d: %f, |y%d-w%d|: %f"%(i,t,i,w,i,realfunc(t),i,i,abs(realfunc(t)-w)))
		else:
			print ("t%d: %f, w%d: %f "%(i,t,i,w))
		value.append(t)
		res.append(w)
	return value,res

def MidPoint(func,a,b,n,alpha,realfunc=None):
	h=(b-a)/n
	t=a
	w=alpha
	if realfunc is not None:
		print ("t0: %f, w0: %f, y0: %f, |y0-w0|: %f"%(t,w,realfunc(t),abs(realfunc(t)-w)))
	else:
		print ("t0: %f, w0: %f"%(t,w))

	value=[]
	res=[]
	value.append(t)
	res.append(w)
	for i in range(1,n+1):
		w+=h*func(w+h/2*(func(w,t)),t+h/2)
		t=a+i*h
		if realfunc is not None:
			print ("t%d: %f, w%d: %f, y%d: %f, |y%d-w%d|: %f"%(i,t,i,w,i,realfunc(t),i,i,abs(realfunc(t)-w)))
		else:
			print ("t%d: %f, w%d: %f "%(i,t,i,w))
		value.append(t)
		res.append(w)
	return value,res

# to do other order
def RungeKutta(func,a,b,n,alpha,order=4,realfunc=None):
	h=(b-a)/n
	t=a
	w=alpha
	if realfunc is not None:
		print ("t0: %f, w0: %f, y0: %f, |y0-w0|: %f"%(t,w,realfunc(t),abs(realfunc(t)-w)))
	else:
		print ("t0: %f, w0: %f"%(t,w))
	value=[]
	res=[]
	value.append(t)
	res.append(w)
	for i in range(1,n+1):
		K1 = h*func(w, t);
		K2 = h*func(w + K1/2,t + h/2)
		K3 = h*func(w + K2/2,t + h/2)
		K4 = h*func(w + K3,t + h)
		w = w + (K1 + 2*K2 + 2*K3 + K4)/6
		t = a + i*h
		if realfunc is not None:
			print ("t%d: %f, w%d: %f, y%d: %f, |y%d-w%d|: %f"%(i,t,i,w,i,realfunc(t),i,i,abs(realfunc(t)-w)))
		else:
			print ("t%d: %f, w%d: %f "%(i,t,i,w))
		value.append(t)
		res.append(w)
	return value,res

if __name__== "__main__":
	def func1(y,t):
		return math.cos(2*t)+math.sin(3*t)-0.25*math.sin(2*t)+3.0/8*math.cos(3*t)
	value,res=Euler(func1,0.0,1.0,4,1)

	def func2(y,t):
		return (1+t)/(1+y)+((1+y)**2-(1+t)**2)/(1+y)**3/4
	value,res=Euler(func2,1.0,2.0,2,2)

	def func3(y,t):
		return 1.0+y/t+1.0/8/t-1.0/96/t/t+1.0/768/t/t/t
	value,res=Euler(func3,1.0,2.0,4,2)

	def func4(y,t):
		return 1.0+(t-y)**2
	def realfunc4(t):
		return t+1.0/(1-t)
	value,res=MidPoint(func4,2.0,3.0,2,1,realfunc=realfunc4)

	def func5(y,t):
		return (y/t)-(y/t)**2
	def realfunc5(t):
		return t/(1+math.log(t))
	value,res=MidPoint(func5,1.0,2.0,10,1,realfunc=realfunc5)

	value,res=RungeKutta(func4,2.0,3.0,2,1,realfunc=realfunc4)



