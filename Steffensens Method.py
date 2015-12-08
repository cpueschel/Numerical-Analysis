#Steffensen's Method
import math
import fractions
#Function
def calcfunction(x):
	return (1 + (math.sin(x))**2)
print "-------------------------------------------------------------------------"
print "Steffensen's Method"
#Inputs
p0 = 1.0
tol = 10**(-5)
max_it = 1000
i = 1

while i < max_it:
	p1 = calcfunction(p0)
	p2 = calcfunction(p1)
	p = p0 - ((p1-p0)**2)/(p2 - 2*p1 + p0)
	print p
	if math.fabs(p-p0) < tol:
		print "Solution for p = %f with a tolerance less than %f" % (p,tol)
		break
	i = i+1
	p0=p

print "Method Finished after %d iterations!" % (i)
print "-------------------------------------------------------------------------"



