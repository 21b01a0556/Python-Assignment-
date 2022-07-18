
from array import *
a=array('i',[1,4,2,6,8,3,10])      
ele=int(input("Enter search element"))
flag=0
for i in range(len(a)):
        if(a[i] == ele):
            flag=i+1
            break
        else:
             pass
if(flag == 0):
    print("Not found")
else:
    print('Element found in',flag,'position')