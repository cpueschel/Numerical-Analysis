#Rhomburg Integration
import math
import fractions
#Function
def calcfunction(x):
	return ((math.cos(x))**2)

print "-------------------------------------------------------------------------"
print "Romburg Integration"
#Inputs
a = -1.0
b = 1.0
n = 10
diff = 10.0
R = [[0.0 for f in xrange(n)] for f in xrange(n)] 
sum = 0
h = b-a
R[1][1] = (h/2)*(calcfunction(a) + calcfunction(b))
print "R[1][1] = %.10f" % (R[1][1])
print "----------------------"
for i in range(2,n):

	
	for ii in range(1,int(math.pow(2,i-2))+1):
		sum = sum + calcfunction(a + (ii-0.5)*h)
	R[2][1]	 = (R[1][1] + h*sum)/2

	print "R[2][1] = %.10f" % (R[2][1])
	for j in range(2,i+1):
		R[2][j] = R[2][j-1] + ( (R[2][j-1] - R[1][j-1]) / (math.pow(4,j-1) - 1) )
	for j in range(1,i+1):
		print "R[%d][%d] = %.10f" % (i,j,R[2][j])
		R[1][j] = R[2][j]

	print "----------------------"
	h = h/2
	sum = 0

	
	print diff
print "-------------------------------------------------------------------------"



