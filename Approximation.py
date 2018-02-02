import math

# To find a solution to f (x) = 0 given an initial approximation p0:
def NewtonAppro(func,func_der,p0,TOL,max_iter):
	print("P0:%.10f"%(p0))
	for i in range(max_iter):
		p=p0-func(p0)/func_der(p0)
		print("P%d:%.10f"%(i+1,p))
		if(abs(p-p0)<TOL):
			return p
		p0=p
	return p

# To find a solution to f (x) = 0 given an initial approximation p0,p1:
def SecantAppro(func,p0,p1,TOL,max_iter):
	q0=func(p0)
	q1=func(p1)
	print("P0:%.10f"%(p0))
	print("P1:%.10f"%(p1))
	for i in range(max_iter):
		p = p1 - q1*(p1 - p0)/(q1 - q0)
		print("P%d:%.10f"%(i+2,p))
		if(abs(p-p1)<TOL):
			return p
		p0 = p1
		q0 = q1
		p1 = p
		q1 = func(p)
	return p

# To find a solution to f (x) = 0 given the continuous function f on the interval [p0, p1] where f (p0) and f (p1) have opposite signs
def FalsePosAppro(func,p0,p1,TOL,max_iter):
	q0=func(p0)
	q1=func(p1)
	assert q0*q1<0
	print("P0:%.10f"%(p0))
	print("P1:%.10f"%(p1))
	for i in range(max_iter):
		p = p1 - q1*(p1 - p0)/(q1 - q0)
		print("P%d:%.10f"%(i+2,p))
		if(abs(p-p1)<TOL):
			return p
		q = func(p)
		if q * q1 < 0:
			p0 = p1
			q0 = q1
		p1 = p
		q1 = q
	print("The procedure was unsuccessful after %d iterations"%(max_iter))
	return None


if __name__== "__main__":
	def func1(x):
		x=1.0*x
		return -x**3-math.cos(x)

	SecantAppro(func1,-1,0,0,3-1)

	def func2(x):
		x=1.0*x
		return x**3-2*x**2-5
	def func2_der(x):
		x=1.0*x
		return 3*x**2-4*x
	NewtonAppro(func2,func2_der,4,1e-4,100)

	def func3(x):
		x=1.0*x
		return math.exp(x) + 2 ** (0 - x) + 2 * math.cos(x) - 6
	SecantAppro(func3,1,2,1e-5,100)


