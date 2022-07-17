n=int(input("Enter the number:"))
lst=[]
for i in range(2,n+1):
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime:
        lst.append(i)
    
print(lst)
