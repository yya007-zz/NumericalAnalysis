import math
import numpy as np

def naturalCubicSpine(numberList,valueList):
	n=valueList.shape[0]-1
	a=np.zeros([n+1])
	b=np.zeros([n+1])
	c=np.zeros([n+1])
	d=np.zeros([n+1])
	
	h=np.zeros([n+1])
	l=np.zeros([n+1])
	u=np.zeros([n+1])
	z=np.zeros([n+1])
	for i in range(n):
		h[i]=numberList[i+1]-numberList[i]

	for i in range(1,n):
		a[i]=3/h[i]*(valueList[i+1]-valueList[i])-3/(h[i-1])*(valueList[i]-valueList[i-1])

	l[0]=1
	for i in range(1,n):
		l[i]=2*(numberList[i+1]-numberList[i-1])-h[i-1]*u[i-1]
		u[i]=h[i]/l[i]
		z[i]=(a[i]-h[i-1]*z[i-1])/l[i]
	l[n]=1
	
	# Could use np.linalg.solve

	for i in range(n):
		j = n-1-i
		c[j]= z[j] - u[j]*c[j+1]
		b[j]= (valueList[j+1] - valueList[j] )/h[j] - h[j]*(c[j+1] + 2*c[j])/3
		d[j]= (c[j+1] - c[j] )/(3*h[j])
	
	for i in range(n):
		print("a%d:%10f, b%d:%10f, c%d:%10f, d%d:%10f"%(i,valueList[i],i,b[i],i,c[i],i,d[i]))

if __name__== "__main__":
	naturalCubicSpine(np.array([0.0,1.0,2.0]),np.array([0.0,1.0,2.0]))
	naturalCubicSpine(np.array([0.1,0.2,0.3,0.4]),np.array([-0.62049958,-0.28398668,0.00660095,0.24842440]))