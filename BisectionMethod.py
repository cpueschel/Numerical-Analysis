#This is the function we are using the Bisection Method on.
import math
def calcfunction(x):
	return ((x**3)-25)
	

print "-------------------------------------------------------------------------"
print "Bisection Method"
#Inputs
a = 0.0
b = 5.0
print "f(a) = %f and f(b) = %f" % (calcfunction(a),calcfunction(b))
tol = 10**(-4)
max_it = 1000
i = 1


FA = calcfunction(a)
while i < max_it:
	p = a+(b-a)/2
	FP = calcfunction(p)
	if FP == 0 or (b-a)/2 < tol:
		print "Solution for p = %f with a tolerance less than %f" % (p,tol)
		break
	i = i+1
	if FA*FP > 0:
		a = p
	else:
		b = p
print "Method Finished after %d iterations!" % (i)
print "-------------------------------------------------------------------------"



