#Euler's Method
import math
import fractions
#Function
def calcfunction(t,y):
	return ( -20.0*y + 20.0*math.cos(t) - math.sin(t) )
def actualfunc(t):
	return ( -math.exp(-20*t) + math.cos(t) )
print "-------------------------------------------------------------------------"
print "Euler's Method"
#Inputs
a = 0.0
b = 2.0
h = 0.25
alpha = 0.0


# Step 1
t = a
w = alpha
error = w - actualfunc(t)
N = int((b-a)/h)
print "t|w|error"
print "%.2f|%.10f|%.10f" %(t,w,math.fabs(error))

for i in range(1,N+1):
	w = w+h*calcfunction(t,w)
	t = a+i*h
	error = w - actualfunc(t)
	print "%.2f|%.10f|%.10f" % (t,w,math.fabs(error))
print "-------------------------------------------------------------------------"


