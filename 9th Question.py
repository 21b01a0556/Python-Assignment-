import math
class QuadraticEquation:
 def __init__(self,a,b,c):
  self.__a = a
  self.__b = b
  self.__c = c
 def getA(self):
  return self.__a
 def getB(self):
  return self.__b
 def getC(self):
  return self.__c
 def getDiscriminant(self):
  return (self.__b**2) - (4 * self.__a * self.__c)
 def getRoot1(self):
  if self.getDiscriminant()<0:
   return 0
  else:
   D = self.getDiscriminant()
   B = self.getB()
   return (-B + math.sqrt(D))/(2*self.__a)
 def getRoot2(self):
  if self.getDiscriminant()<0:
   return 0
  else:
   D = self.getDiscriminant()
   B = self.getB()
   return (-B - math.sqrt(D))/(2*self.__a)

#Driver Code
a = int(input("Enter a:\t"))
b = int(input("Enter b:\t"))
c = int(input("Enter c:\t"))
obj = QuadraticEquation(a,b,c)
print("Get a:\t",obj.getA())
print("Get b:\t",obj.getB())
print("Get c:\t",obj.getC())
D = obj.getDiscriminant()
if D > 0:
 print("real and unequal roots")
 print("Root1 :\t",obj.getRoot1())
 print("Root1 :\t",obj.getRoot2())
elif D == 0:
 print("real and equal roots")
 print("Root :\t",obj.getRoot1())
else:
 print("Complex Roots")