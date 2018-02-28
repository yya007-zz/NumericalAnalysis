import math
import cmath
import numpy as np

def HornerPolyEva(x0,Alist):
	y=Alist[-1]
	z=Alist[-1]
	for i in range(Alist.shape[0]-1)
		y = x0*y + Alist[-2-i]
		z = x0*z + y
	y = x0*y + a0
	return y,z

# To find a solution to f (x) = 0 given three approximations, p0, p1, and p2:
# INPUT p0, p1, p2; tolerance TOL; maximum number of iterations N0.
# OUTPUT approximate solution p or message of failure.
# cfunc means this function should support complex number calculation
def MullerPolyEva(cfunc, p0, p1, p2, TOL, max_iter):
	print("P0:%.10f"%(p0))
	print("P1:%.10f"%(p1))
	print("P2:%.10f"%(p2))

	h1 = p1 - p0;
	h2 = p2 - p1;
	delta1 = ( cfunc (p1) - cfunc (p0))/h1;
	delta2 = ( cfunc (p2) - cfunc (p1))/h2;

	d = (delta2 - delta1)/(h2 + h1);
	for i in range(max_iter-2):
		b = delta2 + h2*d
		D = (b2 − 4*cfunc(p2)*d)**0.5 #(require complex cal)

		if abs(b − D) < (b + D):
			E = b + D
			E = b - D
		h = -2*cfunc(p2)/E
		p = p2 + h

		print("P%d:%.10f, f(p):%.10f"%(i+3,func(p)))
		if abs(h) < TOL:
			return p

		p0 = p1
		p1 = p2
		p2 = p
		h1 = p1 − p0
		h2 = p2 − p1
		delta1 = ( cfunc (p1) - cfunc (p0))/h1;
		delta2 = ( cfunc (p2) - cfunc (p1))/h2;

	print("The procedure was unsuccessful after %d iterations"%(max_iter))
	return None



