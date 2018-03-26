import math
import numpy as np

def GaussianElimination(E):
	n=E.shape[0]
	m=np.copy(E)
	x=np.zeros(n)
	for i in range(n-1):
		if np.sum(m[i:,i])==0:
			print("no unique solution exists")
			return None
		else:
			p=i
			for k in range(i+1,n):
				if m[p,i]==0:
					p=k
				if abs(m[k,i])<abs(m[p,i]) and m[k,i]!=0:
					p=k 
		if p!=i:
			m[[p,i]] = m[[i,p]]
		for j in range(i+1,n):
			coeff = m[j,i] / m[i,i]
			m[j,:]=m[j,:]-coeff*m[i,:]
	if(m[n-1,n-1]==0):
		print("no unique solution exists")
		return None
	x[-1]=m[n-1,n]/m[n-1,n-1]
	print m
	for i in range(n-2,-1,-1):
		x[i] = (m[i,n]-np.sum(m[i,i+1:n]*x[i+1:]))/m[i,i]
	res=""
	for i in range(len(x)):
		res+=("x%d: %f "%(i+1,x[i]))
	print (res)

if __name__== "__main__":
	E=[[1,1,-1,1,-1,2],
	[2,2,1,-1,1,4],
	[3,1,-3,-2,3,8],
	[4,1,-1,4,-5,16],
	[16,-1,1,-1,-1,32]]

	GaussianElimination(np.array(E,dtype=float))

