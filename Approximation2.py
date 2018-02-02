import math
import numpy as np

#Generate the array with given function
def PlistGen(P0,func,K=5):
	Plist=[]
	Plist.append(P0)
	for i in range(K):
		P=func(Plist)
		print("P%d:%.10f"%(i+1,p))
		Plist.append(P)
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
	return Plist-PDelta*PDelta/PDeltaSqure

# To find a solution to p = func(p) given an initial approximation p0
# Pre: initial approximation p0; tolerance TOL; maximum number of iterations N0.
# Post: approximate solution p or message of failure.
def SteffensenAppro(func,p0,TOL,max_iter):
	print("P0:%.10f"%(p0))
	for i in range(max_iter):
		p1 = func(p0); #(Compute p(i−1)1 .)
		p2 = func(p1); #(Compute p(i−1)2 .)
		p = p0 − (p1 − p0)2/(p2 − 2p1 + p0). #(Compute p(i )0 .)
		print("K:%.10f, P0:%.10f, P1:%.10f, P2:%.10f"%(i,p0,p1,p2))
		if(abs(p-p0)<TOL):
			return p
		p0=p
	print("The procedure was unsuccessful after %d iterations"%(max_iter))
	return None

if __name__== "__main__":
	def func1(Plist):
		return 3**(-Plist(-1))
	Plist=PlistGen(P0,func1,K=5)

	


