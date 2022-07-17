def factor(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    print("Factors of ",n," are ",lst)
n=int(input("Enter the number:"))
print(factor(n))
