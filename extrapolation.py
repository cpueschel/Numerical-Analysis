#Extrapolation Method
import math
import fractions
#Function
def calcfunction(t,y):
    return ( (2.9*(10**(-2)))*y - (1.4*(10**(-7))*(y**2)))

print "-------------------------------------------------------------------------"
print "#Extrapolation Algorithm"
print "TO 	 | W	 | 	h"

#Intialize
t =  [0.0]*100
w =  [0.0]*100
y =  [0.0]*100
NK = [0.0,2.0,4.0,6.0,8.0,12.0,16.0,24.0,32.0]
Q = [[0.0 for f in xrange(100)] for f in xrange(100)] 

#Inputs
a = 0.0
b = 5.0
hmin = 0.02
hmax = 0.25
alpha = 50976
TOL = 10**(-4)


TO = a
WO = alpha
h = hmax
FLAG = 1

for i in range(1,8):
	for j in range(1,i+1):
		Q[i][j] = (NK[i+1]/ NK[j])**2
while (FLAG == 1):
	k = 1
	NFLAG = 0
	while (k <= 8 and NFLAG == 0):
		HK = h/NK[k]
		T = TO
		W2 = WO
		W3 = W2 + HK*calcfunction(T,W2)
		T = TO + HK
		
		for j in range(1,int(NK[k])):
			W1 = W2
			W2 = W3
			W3 = W1 + 2.0*HK*calcfunction(T,W2)
			T = TO + (j+1)*HK
		y[k] = 0.5*( W3 + W2 + HK*calcfunction(T,W3) )
		if (k >= 2):
			j = k
			v = y[1]
			while (j >= 2):
				y[j-1] = y[j] + (( y[j] - y[j-1])/(Q[(k-1)][(j-1)] -1.0 ))
				j = j - 1
			#print "T?F = ",(math.fabs(y[1] - v) <= TOL), " | j = ", k
			if (math.fabs(y[1] - v) <= TOL):
				NFLAG = 1
			else: 
				NFLAG = 0



		k = k + 1
	k = k - 1

	if (NFLAG == 0): #Steps 17 and 18
		h = 0.5*h
		print h
		if (h < hmin):
			print "hmin exceeded"
			FLAG = 0
	else: #Steps 19 and 20		
		WO = y[1]
		TO = TO + h
		print "%.10f | %.10f | %.10f" % (TO,WO,h)
		
		if (TO >= b):
			FLAG = 0

		if ((TO + h) > b):
			h = b - TO

		if (k <= 3 and h < 0.5*hmax):
			h = 2.0*h
		

