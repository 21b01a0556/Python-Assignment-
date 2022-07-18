#6th question a)
from array import *
a=array('i',[1,4,2,6,8,3,10])  
print(a)    
ele=int(input("Enter search element:\t"))
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
    
#6th question b)
s=input("Enter a string:\t")
l=0
j=0
m=0
k=0
for i in range(len(s)):
    if(s[i].isupper()):
        l=l+1
    elif(s[i].islower()):
        j=j+1
    elif(s[i].isnumeric()):
        m=m+1
    else:
        k=k+1
     
print('No of uppercase letters: ',l)
print('No of lowercase letters: ',j)
print('No of numericals: ',m)
print('No of special characters',k)