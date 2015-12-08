#Modified Newton's Method
import math
import fractions
#Function
def calcfunction(x):
	return (math.exp(3*x)-27*(x**6)+27*(x**4)*math.exp(x)-9*(x**2)*math.exp(2*x))
#Function Derivative
def calcfunctionDeriv(x):
	return (3*math.exp(3*x)-162*(x**5)+108*(x**3)*math.exp(x)+27*(x**4)*math.exp(x)-18*x*math.exp(2*x)-18*(x**2)*math.exp(2*x))
def calcfunction2ndDeriv(x):
	return (9*math.exp(3*x) - 810*(x**4) + 216*(x**3)*math.exp(x) + 324*(x**2)*math.exp(x) + 27*(x**4)*math.exp(x) - 18*math.exp(2*x) - 72*x*math.exp(2*x) - 36*(x**2)*math.exp(2*x))	
print "-------------------------------------------------------------------------"
print "Modified Newton's Method"
#Inputs
p0 = 3.0
tol = 10**(-5)
max_it = 1000
i = 1

while i < max_it:
	p =p0 - (calcfunction(p0)*calcfunctionDeriv(p0))/((calcfunctionDeriv(p0)**2) - (calcfunction(p0)*calcfunction2ndDeriv(p0)))
	print p
	if math.fabs(p-p0) < tol:
		print "Solution for p = %f with a tolerance less than %f" % (p,tol)
		break
	i = i+1
	p0=p

print "Method Finished after %d iterations!" % (i)
print "-------------------------------------------------------------------------"



