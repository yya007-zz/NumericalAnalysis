import math
import cmath
import numpy as np

#Generate the array with given function
def PlistGen(p0,func,K=5):
	Plist=[]
	Plist.append(p0)
	for i in range(K):
		p=func(Plist)
		Plist.append(p)
	return np.array(Plist)

# To find a solution to f (x) = 0 given an initial approximation p0:
def NewtonAppro(func,func_der,p0,TOL,max_iter):
	Plist=[]
	Plist.append(p0)
	for i in range(max_iter):
		p=p0-func(p0)/func_der(p0)
		Plist.append(p)
		if(abs(p-p0)<TOL):
			return np.array(Plist)
		p0=p
	return np.array(Plist)

def PlistPrint(Plist):
	for i in range(Plist.shape[0]):
		print("P%d:%.10f"%(i,Plist[i]))
	return np.array(Plist)

def AitkenDelta(Plist,K=1):
	Phat=Plist
	for i in range(K):
		Phat=Phat[1:]-Phat[:-1]
	return Phat

# P-(P1-P)**2/(P2-2P1+P)
def AitkenDeltaSquareAcc(Plist):
	PDelta=AitkenDelta(Plist,K=1)
	PDeltaSqure=AitkenDelta(Plist,K=2)
	return Plist[:-2]-PDelta[:-1]*PDelta[:-1]/PDeltaSqure

# To find a solution to p = func(p) given an initial approximation p0
# Pre: initial approximation p0; tolerance TOL; maximum number of iterations N0.
# Post: approximate solution p or message of failure.
def SteffensenAppro(func,p0,TOL,max_iter):
	for i in range(max_iter):
		p1 = func(p0) #(Compute p(i-1)1)
		p2 = func(p1) #(Compute p(i-1)2)
		p = p0 - (p1 - p0)**2/(p2 - 2*p1 + p0)#(Compute p(i)0)
		print("K:%d, P0:%.10f, P1:%.10f, P2:%.10f"%(i,p0,p1,p2))
		if(abs(p-p0)<TOL):
			print("K:%d, P0:%.10f"%(i+1,p))
			return p
		p0=p
	print("The procedure was unsuccessful after %d iterations"%(max_iter))
	return None
	
if __name__== "__main__":
	def func1(Plist):
		return 3**(-Plist[-1])
	Plist=PlistGen(0.5,func1,K=6)
	print("P:")
	PlistPrint(Plist)
	Plist=AitkenDeltaSquareAcc(Plist)
	print("P hat:")
	PlistPrint(Plist)

	def func2(x):
		x=1.0*x
		return math.exp(6*x)+3*math.log(2)**2*math.exp(2*x)-math.log(8)*math.exp(4*x)-math.log(2)**3
	
	def func2_der(x):
		x=1.0*x
		return 6*math.exp(6*x)+2*3*math.log(2)**2*math.exp(2*x)-4*math.log(8)*math.exp(4*x)

	Plist=NewtonAppro(func2,func2_der,0,TOL=2*1e-4,max_iter=100)
	print("P:")
	PlistPrint(Plist)
	Plist=AitkenDeltaSquareAcc(Plist)
	print("P hat:")
	PlistPrint(Plist[:11])

	def func3(x):
		x=1.0*x
		return (2-math.exp(x)+x**2)/3
	SteffensenAppro(func3,0.5,TOL=1e-5,max_iter=100)


