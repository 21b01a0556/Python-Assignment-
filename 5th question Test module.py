#Test.py
import Prime
from Prime import *
print("The first 50 prime numbers are:")
k = 1
i = 2
while k<100:
	if isPrime(i):
		k+=1
		print(i,end =" ")
		i+=1
	else:
		i+=1
	
print("\nPrime numbers upto 100 are:")
for c in range(2,101):
	if isPrime(c):
		print(c,end = " ")
	
print("\nEmirp numbers upto 100 are:")
for c in range(2,101):
	if isEmirp(c):
		print(c,end = " ")
	
print("\nMersenne numbers upto 100 are:")
for c in range(2,33):
	if mersennePrime(c):
		print(c,end = " ")
	
print("\nTwin prime numbers below 100")
printTwinPrime(200)	
