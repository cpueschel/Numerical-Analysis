#Runge-Kutta Method for Systems of Differential Equations
import math
import fractions
#Function
def calcfunction1(t,u1,u2):
    return ( u2 )
def calcfunction2(t,u1,u2):
    return ( (-3.0/t) + (4.0/(t**2))*u1 - (1.0/t)*u2 )
def actualfunction1(t):
    return ( 2.0*(t**2) + t +(1.0/(t**2)) )
def actualfunction2(t):
    return ( 4.0*t + 1.0 - 2.0*(1.0/(t**3)) )

#Variable
alpha =  [0.0]*100
w =  [0.0]*100
u1 =  [0.0]*100
u2 =  [0.0]*100
k = [[0.0 for f in xrange(100)] for f in xrange(100)]

a = 1.0
b = 3.0
m = 2 #Number of Equations

h = 0.2
N = int((b-a)/h)
alpha[1] = 4.0
alpha[2] = 3.0

#h = (b-a)/N
t = a

print "    ti    |    u1,i        |    w1,i        |    u2,i        |    w2,i    |    Act. Error1    |    Act. Error 2"
for j in range(1,m+1):
    w[j] = alpha[j]
u1[0] = actualfunction1(t)
u2[0] = actualfunction2(t)

print "%.10f|%.10f|%.10f|%.10f|%.10f|%.10f|%.10f" % (t,u1[0],w[1],u2[0], w[2], (math.fabs(u1[0]-w[1])),math.fabs(u2[0]-w[2]))
for i in range(1,N+1):
    # i = 1
    k[1][1] = h*calcfunction1(t,w[1],w[2])
    k[1][2] = h*calcfunction2(t,w[1],w[2])
    # i = 2
    k[2][1] = h*calcfunction1( (t + 0.5*h), w[1] + 0.5*k[1][1], w[2] + 0.5*k[1][2])
    k[2][2] = h*calcfunction2( (t + 0.5*h), w[1] + 0.5*k[1][1], w[2] + 0.5*k[1][2])
    # i = 3
    k[3][1] = h*calcfunction1( (t + 0.5*h), w[1] + 0.5*k[2][1], w[2] + 0.5*k[2][2])
    k[3][2] = h*calcfunction2( (t + 0.5*h), w[1] + 0.5*k[2][1], w[2] + 0.5*k[2][2])
    # i = 4
    k[4][1] = h*calcfunction1( t+h, w[1] + k[3][1], w[2] + k[3][2])
    k[4][2] = h*calcfunction2( t+h, w[1] + k[3][1], w[2] + k[3][2])

    for j in range(1,m+1):
        w[j] = w[j] + (k[1][j] + 2.0*k[2][j] + 2.0*k[3][j] + k[4][j])/6.0

    #Calculate Actual u1 and u2

    t = a + i*h
    u1[i] = actualfunction1(t)
    u2[i] = actualfunction2(t)
    print "%.10f|%.10f|%.10f|%.10f|%.10f|%.10f|%.10f" % (t,u1[i],w[1],u2[i], w[2],(math.fabs(u1[i]-w[1])),math.fabs(u2[i]-w[2]))
