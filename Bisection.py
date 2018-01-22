import math

# TO DO: extend to general case
def bisection(func, left, right, precision = 1e-5):
	if left>right:
		print("left boundary is large than right boundary, exchange boundary.")
		return bisection(func, right, left, precision)

	lvalue=func(left)
	rvalue=func(right)
	
	print("f(%.10f)= %.10f, f(%.10f)= %.10f" % (left,lvalue,right,rvalue))

	if lvalue*rvalue>0:
		print("No root lies between %.10f and %.10f.f" % (left, right))
		return left
	
	newright=right
	newleft=left
			
	while(True):
		lvalue=func(newleft)
		rvalue=func(newright)
		mid=(newright+newleft)/2.0
		mvalue=func(mid)
		if mvalue==0:
			return mid
			print ("The root is %f" % (mid))

		print("Therefore, the root lies between %.10f and %.10f." % (newleft, newright)) 
		print("")
		print("The middle value between %.10f and %.10f is %.10f. \nf(%.10f) = %.10f, f(%.10f) = %.10f, f(%.10f) = %.10f" % (newleft, newright, mid, newleft, lvalue,  mid, mvalue, newright, rvalue)) 
		
		if mvalue*lvalue<0:
			newright=mid
		else:
			newleft=mid
		

		if abs(mvalue-0)<precision:
			print("|f(%.10f)|= %.10f < %.10f" % (mid,abs(mvalue-0),precision))
			print("The accuracy is within the %.10f"%(precision))
			print("Hence %.10f gives approximate solution." % (mid))
			return mid
		 


def fixedpoint(func, start, precision = 1e-5):

	last=start
	print(last)
	while(True):
		current=func(last)
		print(current)
		
		if abs(current-last)<precision:
			print("Hence %.10f gives approximate solution." % (current))
			return current
		last=current

if __name__== "__main__":
	def func1(x):
		return 2*x*math.cos(2*x)-(x + 1)**2

	bisection(func1,-3,-2)
	print("")
	print("")
	bisection(func1,-1,0)

	def func2(x):
		return 32.17*(math.exp(x)-math.exp(-x)-2*math.sin(x))+6.8*x**2

	print("")
	print("")
	bisection(func2,-0.4,-0.3)

	

	def func3(x):
		return (2-math.exp(x)+x**2)/3.0

	def func4(x):
		return 5/x**2+2

	fixedpoint(func3, 0.5)
	print("")
	print("")
	fixedpoint(func4, 2.5)

