#Adams Step-Size Predictor-Corrector Method
import math
import fractions
#Function
def calcfunction(t,y):
	return (  (t + 2.0*(t**3))*(y**3) - t*y )
def actualfunc(t):
	return ( 1.0/math.sqrt(3.0+ 2.0*(t**2) + 6.0*math.exp(t**2)   )) 

print "-------------------------------------------------------------------------"


#Intialize
t =  [0.0]*10000
w =  [0.0]*10000
x =  [0.0]*10000
v =  [0.0]*10000
K =  [0.0]*10000
#Inputs
TOL = 10.0**(-6.0)
a = 0.0
b = 2.0
hmin = 0.0000000000000002
hmax = 0.5
alpha = (1.0/3.0)



h = hmax
FLAG = 1
LAST = 0

print "#Adams-Moulton Methods: Four-Step Explicit Method"
print "    t     |    w       | h  |    Actual Error"
t[0] = a
t[1] = a + h
t[2] = a + 2*h
t[3] = a + 3*h
w[0] = alpha
w[1] = actualfunc(a+h)
w[2] = actualfunc(a+2*h)
w[3] = actualfunc(a+3*h)

for i in range(0,3):
	print "%.10f|%.10f|%.10f|0.0000" % (t[i],w[i],h)

for i in range(3,7):
	t[i+1] = t[i] + h
	w[i+1] = w[i] + (h/720.0)*(251.0*calcfunction(t[i+1],w[i+1]) + 646.0*calcfunction(t[i],w[i]) - 264.0*calcfunction(t[i-1],w[i-1]) + 106.0*calcfunction(t[i-2],w[i-2]) - 19.0*calcfunction(t[i-3],w[i-3]) )
	error = actualfunc(t[i+1]) - w[i+1]
	#print "%.10f|%.10f|%.10f" % (t[i+1],w[i+1],math.fabs(error))



#for j in range(1,4):
#	K[1] = h*calcfunction(t[j-1],w[j-1])
#	K[2] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[1]*0.5))
#	K[3] = h*calcfunction( (t[j-1] +.5*h) , (w[j-1] + K[2]*0.5))
#	K[4] = h*calcfunction( (t[j-1] + h) , (w[j-1] + K[3]))
#	w[j] = w[j-1] + (( K[1]+2.0*K[2]+2.0*K[3]+K[4]) / 6.0 )
#	t[j] = t[j-1] + h


NFLAG = 1
i = 7
t_current = t[6] + h

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

				error = actualfunc(t[j]) - w[j]
				#if (i % 25) == 1:
				print "%.10f|%.10f|%.10f|%.10f" % (t[j],w[j],h,math.fabs(error))
		else:
			#if (i % 25) == 1:
			error = actualfunc(t[j+1]) - w[j+1]
			print "%.10f|%.10f|%.10f|%.10f" % (t[i],w[i],h,math.fabs(error))
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

			for ii in range(i,i+5):
				t[ii+1] = t[ii] + h
				w[ii+1] = w[ii] + (h/720.0)*(251.0*calcfunction(t[ii+1],w[ii+1]) + 646.0*calcfunction(t[ii],w[ii]) - 264.0*calcfunction(t[ii-1],w[ii-1]) + 106.0*calcfunction(t[ii-2],w[ii-2]) - 19.0*calcfunction(t[ii-3],w[ii-3]) )

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

			for ii in range(i-1,i+5):
				t[ii+1] = t[ii] + h
				w[ii+1] = w[ii] + (h/720.0)*(251.0*calcfunction(t[ii+1],w[ii+1]) + 646.0*calcfunction(t[ii],w[ii]) - 264.0*calcfunction(t[ii-1],w[ii-1]) + 106.0*calcfunction(t[ii-2],w[ii-2]) - 19.0*calcfunction(t[ii-3],w[ii-3]) )

		    	i = i + 3
		    	NFLAG = 1
	t_current = t[i-1] + h

