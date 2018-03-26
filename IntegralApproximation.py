import math
import numpy as np

# To approximate the integral f(x) on region a b
def CompositeSimpson(func,a,b,n):
	h=(b-a)/n
	XI0 = func(a) + func(b);
	XI1 = 0.0
	XI2 = 0.0
	for i in range(1,n):
		X = a + i*h
		if i%2 == 0:
			XI2 += func(X)
		else:
			XI1 += func(X)
	XI = h*(XI0 + 2*XI2 + 4*XI1)/3.0
	return XI

def CompositeTrapezoidal(func,a,b,n):
	h=(b-a)/n
	XI0 =-(func(a) + func(b));
	for i in range(n+1):
		x = a + i*h
		XI0+=2*func(x)
		print("f(%f): %f"%(x,func(x)))
	return XI0*h/2

def Romberg(func,a,b,n):
	h = (b - a)
	R = np.zeros([3,n+1])
	R[1,1] = h/2*(func(a) + func(b))
	print("R1,1: %f"%(R[1,1]))

	for i in range(2,n+1):
		R[2,1]=0.5*R[1,1]
		for k in range(1,2**(i-2)+1):
			R[2,1]+=0.5*h*func(a + (k - 0.5)*h)
		for j in range(2,i+1):
			R[2,j]= R[2,j-1]+(R[2,j-1]-R[1,j-1])/(4**(j-1)-1)
		for j in range(1,i+1):
			print("R%d,%d: %f"%(i,j,R[2,j])),
		print("")
		h=h/2
		for j in range(1,i+1):
			R[1,j]=R[2,j]
	return R[2,1:]

# def Euler(func,a,b,n,alpha,realfunc=None):
# 	h=(b-a)/n
# 	t=a
# 	w=alpha
# 	if realfunc is not None:
# 		print ("t0: %f, w0: %f, y0: %f, |y0-w0|: %f"%(t,w,realfunc(t),abs(realfunc(t)-w)))
# 	else:
# 		print ("t0: %f, w0: %f"%(t,w))

# 	value=[]
# 	res=[]
# 	value.append(t)
# 	res.append(w)
# 	for i in range(1,n+1):
# 		w+=h*func(w,t)
# 		t=a+i*h
# 		if realfunc is not None:
# 			print ("t%d: %f, w%d: %f, y%d: %f, |y%d-w%d|: %f"%(i,t,i,w,i,realfunc(t),i,i,abs(realfunc(t)-w)))
# 		else:
# 			print ("t%d: %f, w%d: %f "%(i,t,i,w))
# 		value.append(t)
# 		res.append(w)
# 	return value,res

if __name__== "__main__":
	def func1(x):
		return 2.0/(x**2+4)
	print(CompositeTrapezoidal(func1,0.0,2.0,6))
	def func2(x):
		return math.cos(x)**2
	print(CompositeTrapezoidal(func2,-0.5,0.5,4))

	print(CompositeSimpson(func1,0.0,2.0,6))
	print(CompositeSimpson(func2,-0.5,0.5,4))

	def func3(x):
		return x**2*math.log(x)
	Romberg(func3,1.0,1.5,3)
	def func4(x):
		return 2.0/(x**2-4)
	Romberg(func4,0.0,0.35,3)

	def func5(y,t):
		return -5*y+5*(t**2)+2*t
	Euler(func5,0.0,1.0,10,1.0/3)
	def func6(y,t):
		return -t*y+4*t/y
	Euler(func6,0.0,1.0,10,1.0)
	def func7(y,t):
		return 1/t/t-y/t-y**2
	def realfunc7(t):
		return -1.0/t
	value,res=Euler(func7,1.0,2.0,20,-1.0,realfunc7)

