#Runge-Kutta Method for Systems of Differential Equations
import math
import fractions
#Function
def calcfunction1(t,y):
	return ( -20.0*y + 20.0*math.cos(t) - math.sin(t) )

def actualfunction1(t):
	return ( -math.exp(-20*t) + math.cos(t) )

#Variable
alpha =  [0.0]*100
w =  [0.0]*100
u1 =  [0.0]*100
k = [[0.0 for f in xrange(100)] for f in xrange(100)] 

a = 0.0
b = 2.0
m = 1 #Number of Equations

h = 0.25
N = int((b-a)/h)
alpha[1] = 0.0

#h = (b-a)/N
t = a

print "	ti	|	yi = w1,i		|	u1,i		|	Act. Error1	"
w[1] = alpha[1]
u1[0] = actualfunction1(t)


print "%.10f|%.10f|%.10f|%.10f" % (t,w[1],u1[0], (math.fabs(u1[0]-w[1])))
for i in range(1,N+1): 
	# i = 1
	k[1][1] = h*calcfunction1(t,w[1])
	# i = 2
	k[2][1] = h*calcfunction1( (t + 0.5*h), w[1] + 0.5*k[1][1])
	# i = 3
	k[3][1] = h*calcfunction1( (t + 0.5*h), w[1] + 0.5*k[2][1])
	# i = 4
	k[4][1] = h*calcfunction1( t+h, w[1] + k[3][1])


	w[1] = w[1] + (k[1][1] + 2.0*k[2][1] + 2.0*k[3][1] + k[4][1])/6.0

	#Calculate Actual u1 and u2

	t = a + i*h
	u1[0] = actualfunction1(t)

	print "%.10f|%.10f|%.10f|%.10f" % (t,w[1],u1[0],(math.fabs(u1[0]-w[1])))


