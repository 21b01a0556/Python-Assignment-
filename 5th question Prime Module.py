#Prime.py Module
def isPrime(n):
	if n== 1:
		return False
	elif n==2 :
		return True
	else:
		for i in range(2,n):
			if n%i == 0:
				return False
		return True
	
def isPalindromePrime(n):
	if not isPrime(n):
		return False		
	n = str(n)
	if n== "":
		return True
	return n[0] == n[-1] and isPalindrom(n[1:-1])

def isEmirp(n):
	revn = int(str(n)[::-1])
	return isPrime(n) and isPrime(revn)

def mersennePrime(n):
	if isPrime(n):
		return pow(2,n)-1
	
def printTwinPrime(r):
	for i in range(2,r+1):
		for j in range(2,r+1):
			if isPrime(i) and isPrime(j) and j-i==2:
				print(i,',',j,'are Twin Primes')
				
