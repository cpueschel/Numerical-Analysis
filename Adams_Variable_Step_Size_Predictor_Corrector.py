#Adams Step-Size Predictor-Corrector Method
import math
import fractions
#Function
def calcfunction(t,y):
	return ( ( (y/t)**2) + (y/t) )
    
print "-------------------------------------------------------------------------"
print "#Adams Step-Size Predictor-Corrector Method"

#Intialize
t =  [0.0]*100
w =  [0.0]*100
x =  [0.0]*100
v =  [0.0]*100
K =  [0.0]*100
#Inputs
TOL = 10.0**(-4.0)
a = 1.0
b = 1.2
hmin = 0.01
hmax = 0.05
alpha = 1.0

print "    j     |    t           | w            |    h"

t[0] = a
w[0] = alpha
h = hmax
FLAG = 1
LAST = 0

print "0|%.10f|%.10f|%.10f" % (t[0],w[0],h)

for j in range(1,4):
	K[1] = h*calcfunction(t[j-1],w[j-1])
	K[2] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[1]*0.5))
	K[3] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[2]*0.5))
	K[4] = h*calcfunction( (t[j-1] + h) , (w[j-1] + K[3]))
	w[j] = w[j-1] + (( K[1]+2.0*K[2]+2.0*K[3]+K[4]) / 6.0 )
	t[j] = t[j-1] + h


NFLAG = 1
i = 4
t_current = t[3] + h

while (FLAG == 1):
	WP = w[i-1] + (h/24.0)*( 55.0*calcfunction( t[i-1], w[i-1]) - 59.0*calcfunction(t[i-2],w[i-2])  + 37.0*calcfunction(t[i-3],w[i-3]) - 9.0*calcfunction(t[i-4],w[i-4])) #wip
	WC = w[i-1] + (h/24.0)*( 9.0*calcfunction( t_current, WP) + 19.0*calcfunction(t[i-1],w[i-1]) - 5.0*calcfunction(t[i-2],w[i-2]) + calcfunction(t[i-3],w[i-3]) ) #Correct wi
	sig = 19.0*math.fabs(WC - WP)/(270.0*h)
    
	if (sig <= TOL):
		#Steps 7-16
		w[i] = WC
		t[i] = t_current
		if (NFLAG == 1):
			for jj in range(1,5):
				j = i - (4-jj)
				print "%.f|%.10f|%.10f|%.10f" % (j,t[j],w[j],h)
		else:
			print "%.f|%.10f|%.10f|%.10f" % (i,t[i],w[i],h)
		if (LAST == 1):
			FLAG = 0
		else:
			i = i+1
			NFLAG = 0
			if (sig <= TOL) or (t[i-1] + h > b):
				q = (TOL/(2.0*sig))**(0.25)
				if q > 4.0:
					h = 4.0*h
				else:
					h = q*h
			if (h > hmax):
				h = hmax
			if (t[i-1] + 4.0*h > b):
				h = (b - t[i-1])*(1.0/4.0)
				LAST = 1
			for j in range(i,i+3):
				K[1] = h*calcfunction(t[j-1],w[j-1])
				K[2] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[1]*0.5))
				K[3] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[2]*0.5))
				K[4] = h*calcfunction( (t[j-1] + h) , (w[j-1] + K[3]))
				w[j] = w[j-1] + (( K[1]+2.0*K[2]+2.0*K[3]+K[4]) / 6.0 )
				t[j] = t[j-1] + h
		    	NFLAG = 1
		    	i = i + 3
	else: #steps 17-19

		q = (TOL/(2.0*sig))**(0.25)
		if (q < 0.1):
			h = 0.1*h
		else:
			h = q*h
		if (h < hmin):
			FLAG = 0
			print "hmin exceeded"
		else:
			if (NFLAG == 1):
				i = i-3
				for j in range(i,i+3):
				    K[1] = h*calcfunction(t[j-1],w[j-1])
				    K[2] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[1]*0.5))
				    K[3] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[2]*0.5))
				    K[4] = h*calcfunction( (t[j-1] + h) , (w[j-1] + K[3]))
				    w[j] = w[j-1] + (( K[1]+2.0*K[2]+2.0*K[3]+K[4]) / 6.0 )
				    t[j] = t[j-1] + h
		    	i = i + 3
		    	NFLAG = 1
	t_current = t[i-1] + h
