import math
import numpy as np

def newtonDivDiff(numberList,valueList):
	n=valueList.shape[0]-1
	F=np.zeros([n+1,n+1])
	F[:,0]=valueList
	for i1 in range(n):
		i=i1+1
		for j1 in range(i):
			j=j1+1
			F[i,j]=(F[i,j-1]-F[i-1,j-1])/(numberList[i]-numberList[i-j])

	for i in range(n+1):
		print("F %d,%d : %f"%(i,i,F[i,i]))

if __name__== "__main__":
	newtonDivDiff(np.array([-0.1,0,0.2,0.3]),np.array([5.3,2.0,3.19,1.0]))