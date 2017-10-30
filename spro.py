def isPrime(n):
	N = int(n**0.5)
	for i in range(2,N):
		if n%i==0:
			return False
	return True
	
def isPrimeRange(m,n):
	for i in range(m,n):
		if isPrime(i)==True:
			print i
			
def reverse(n):
	rev = 0
	while n>0:
		d=n%10
		n=n/10
		rev = rev*10 + d
	return rev
	
def isPal(n):
	N = reverse(n)
	if n == N:
		return True
	return False
	
def Fibo(n):
	a=0
	b=1
	F = [a,b]
	for i in range(n-2):
		c=a+b
		a=b
		b=c
		F.append(c)
	return F
	
def QuadRoot(a,b,c):
	D = (b**2) - (4*a*c)
	if D == 0 :
		x = -(b/2)
		print "root = ", x
	elif D>0 :
		x1 = (-b+(D**0.5))/2
		x2 = (-b-(D**0.5))/2
		print "roots = ",x1," , ",x2
	else:
			x1 = complex(-b/2,(abs(D)**0.5)/2)
			x2 = complex(-b/2,-(abs(D)**0.5)/2)
			print "roots = ",x1," , ",x2 
