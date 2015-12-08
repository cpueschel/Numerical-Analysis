#Newton's Divided-Difference Formula.
import math
import fractions
#Inputs.
i = 0
xvalue = .43

x = [-2.0,-1.0,0.0,1.0,2.0,3.0]
fx = [1.0,4.0,11.0,16.0,13.0,-4.0] 
n= len(x)

P = [0 for z in range(0,n)]

#Intialize Fij
Fij = [[0 for f in xrange(n)] for f in xrange(n)] 
for i in range(0,n):
	Fij[i][0] = fx[i]
	#print fx[i]
#Output Numbers F0,0 , F1,1, Fn,n
#	Pn(x) = F0,0 + Sum(Fi,i)*Product(-xj)

for i in range(1,n):
	for j in range(1,n):
		Fij[i][j] = (Fij[i][j-1] - Fij[i-1][j-1])/(x[i] - x[i-j])
		#print 'at i = %i and j = %i is Fij is %f' %(i,j,Fij[i][j])

print 'Newton\'s Divided-Difference Formula Solution'		
for i in range(0,n):
	print 'F%i,%i = %f' % (i, i, Fij[i][i])

# Plugging in for f(x)	
P[0] = Fij[0][0]
P[1] = P[0] - Fij[1][1]*(xvalue - x[0])
P[2] = P[1] - Fij[2][2]*(xvalue - x[0])*(xvalue - x[1])
P[3] = P[2] - Fij[3][3]*(xvalue - x[0])*(xvalue - x[1])*(xvalue - x[2])
P[4] = P[3] - Fij[4][4]*(xvalue - x[0])*(xvalue - x[1])*(xvalue - x[2])*(xvalue - x[3])
P[5] = P[4] - Fij[5][4]*(xvalue - x[0])*(xvalue - x[1])*(xvalue - x[2])*(xvalue - x[3])*(xvalue - x[4])
for i in range(0,n):	
	print 'P%i(%f) = %f' %(i,xvalue,P[i])