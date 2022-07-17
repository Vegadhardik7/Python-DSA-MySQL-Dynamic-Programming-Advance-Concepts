def Bigvalue(lst):
    x=lst[0]
    for i in lst:
        if(x<i):
            x=i
    print(x)

def isprime(x):
    return(Bigvalue(x))
lst=[]
n=int(input("Enter the number of elements you want:"))
for i in range(0,n):
    z=int(input("enter the numbers:"))
    lst.append(z)

print(Bigvalue(lst))
print(isprime(lst))
        
