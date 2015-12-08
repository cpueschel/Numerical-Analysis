#Adaptive Quadrature
import math
import fractions
#Function
def calcfunction(x):
	return ((100/(x**2))*math.sin(10/x))

print "-------------------------------------------------------------------------"
print "Adaptive Quadrature"
n = 20
TOL = [0.0 for f in xrange(n)]
a = [0.0 for f in xrange(n)]
h = [0.0 for f in xrange(n)]
FA = [0.0 for f in xrange(n)]
FC = [0.0 for f in xrange(n)]
FB = [0.0 for f in xrange(n)]
L = [0.0 for f in xrange(n)]
S = [0.0 for f in xrange(n)]

#Inputs
a1 = 3.0
b = 1.0
TOL[0] = 10**-4
N = 100
APP = 0.0

S1=0.0
S2=0.0
FD=0.0
FE = 0.0


# i = 1
i = 1
TOL[1] = 10*TOL
a[1] = a1
h[1] = (b - a1)/2
FA[1] = calcfunction(a1)
FC[1] = calcfunction(a1+h[1])
FB[1] = calcfunction(b)
S[1] = h[1]*(FA[1]+4*FC[1]+FB[1])/3

while i >= 0:
	FD = calcfunction(a[i]+h[i]/2)
	FE = calcfunction(a[i]+3*h[i]/2)
	S1 = h[i]*(FA[i]+4*FD+FC[i])/6
	S1 = h[i]*(FC[i]+4*FE+FB[i])/6
	v1 = a[i] 
	v2 = FA[i]
	v3 = FA[i]
	v4 = FB[i]
	v5 = h[i]
	v6 = TOL[i]
	v7 = S[i]
	v8 = L[i]
	
	i = i-1
	
	if math.fabs(S1+S2-v7) < v6:
		APP = APP + S1 + S2
	else: 
		if (v8 >= N):
			print "level exceeded: %d" % (N)
			break
		else: 
			print i
			i = i+1
			a[i] = v1 + v5
			FA[i] = v3
			FC[i] = FC
			FB[i] = v4
			h[i] = v5/2
			TOL[i] = v6/2
			S[i] = S2
			L[i] = v8+1
			
			i = i+1
			a[i] = v1
			FA[i] = v2
			FC[i] = FD
			FB[i] = v3
			h[i] = h[i-1]
			TOL[i] = TOL[i-1]
			S[i] = S1
			L[i] = L[i-1]
						
			
print "APP = %.10f" % (APP)
print "-------------------------------------------------------------------------"