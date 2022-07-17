def factors(n):
    factlst=[]
    for i in range(1,n+1):
        if n%i==0:
            factlst.append(i)
    return(factlst)

def isprime(n):
    return(factors(n)==[1,n])


def primeupto(n):
    primelst=[]
    for i in range(1,n+1):
        if isprime(i):
            primelst.append(i)
    print("prime number upto ",n," are ",primelst)        

n=int(input("Enter the number:"))
print(factors(n))
#print(isprime(n))
print(primeupto(n))
