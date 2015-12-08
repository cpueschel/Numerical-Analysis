#Adams Step-Size Predictor-Corrector Method
import math
import fractions
#Function

#Function
def calcfunction(t,y):
	return (  (t + 2.0*(t**3))*(y**3) - t*y )
def actualfunc(t):
	return ( 1.0/math.sqrt(3.0+ 2.0*(t**2) + 6.0*math.exp(t**2)   ))

print "-------------------------------------------------------------------------"
print "#Adams Step-Size Predictor-Corrector Method"
print "#Adams-Bashforth Method: Five-Step Explicit Method"
#Intialize
t =  [0.0]*10000
w =  [0.0]*10000
x =  [0.0]*10000
v =  [0.0]*10000
K =  [0.0]*10000
#Inputs
TOL = 10.0**(-6.0)
a = 0.0
b = 2.5
hmin = 0.0000000000002
hmax = 0.5
alpha = (1.0/3.0)

print "t           | w            |    h | Actual Error"

h = hmax
FLAG = 1
LAST = 0

t[0] = a
t[1] = a + h
t[2] = a + 2*h
t[3] = a + 3*h
t[4] = a + 4*h
w[0] = alpha
w[1] = actualfunc(a+h)
w[2] = actualfunc(a+2*h)
w[3] = actualfunc(a+3*h)
w[4] = actualfunc(a+4*h)


for i in range(0,5):
	print "%.10f|%.10f|%.10f|0.0000" % (t[i],w[i],h)



NFLAG = 1
i = 5
t_current = t[4] + h

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
				#if (i % 5) == 1:
				error = actualfunc(t[j]) - w[j]
				print "%.10f|%.10f|%.10f|%.10f" % (t[j],w[j],h, math.fabs(error))
		else:
			#if (i % 5) == 1:
			error = actualfunc(t[i]) - w[i]
			print "%.10f|%.10f|%.10f|%.10f" % (t[i],w[i],h, math.fabs(error))
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
#			for j in range(i,i+3):
#				K[1] = h*calcfunction(t[j-1],w[j-1])
#				K[2] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[1]*0.5))
#				K[3] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[2]*0.5))
#				K[4] = h*calcfunction( (t[j-1] + h) , (w[j-1] + K[3]))
#				w[j] = w[j-1] + (( K[1]+2.0*K[2]+2.0*K[3]+K[4]) / 6.0 )
#				t[j] = t[j-1] + h
			for j in range(i-1,i+2):
				t[j+1] = t[j] + h
				w[j+1] = w[j] + (h/720.0)*(1901.0*calcfunction(t[j],w[j]) - 2774.0*calcfunction(t[j-1],w[j-1]) + 2616.0*calcfunction(t[j-2],w[j-2]) - 1274.0*calcfunction(t[j-3],w[j-3]) + 251.0*calcfunction(t[j-4],w[j-4]) )
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
