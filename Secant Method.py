#Secant Method
import math
import fractions
#Function
def calcfunction(x):
	return (math.sin(x)-math.exp(-x))
print "-------------------------------------------------------------------------"
print "Secant Method"
#Inputs
p0 = 6.0
p1 = 7.0
tol = 10**(-5)
max_it = 1000
i = 1

q0= calcfunction(p0)
q1= calcfunction(p1)

while i < max_it:
	#Compute pi
	p =p1 - q1*(p1-p0)/(q1-q0)
	print p
	if math.fabs(p-p0) < tol:
		print "Solution for p = %f with a tolerance less than %f" % (p,tol)
		break
	i = i+1
	p0=p1
	q0=q1
	p1=p
	q1=calcfunction(p) 

print "Method Finished after %d iterations!" % (i)
print "-------------------------------------------------------------------------"



