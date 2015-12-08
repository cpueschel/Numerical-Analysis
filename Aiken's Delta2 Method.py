#Aiken's Delta^2 Method
import math
import fractions
#Function
def calcfunction(x):
	return (x - (math.exp(6*x) + 3*(math.log(2)**2)*math.exp(2*x) - math.log(8)*math.exp(4*x) - math.log(2)**3))
print "-------------------------------------------------------------------------"
print "Aiken's Delta^2 Method"
#Inputs
p0 = 0.0
tol = 2*(10**(-4))
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



