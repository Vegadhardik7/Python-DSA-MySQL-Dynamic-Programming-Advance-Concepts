def facto(n):
    if(n>0):
        x=1
        for i in range(1,n+1):
            if i<=n:
               x=x*i
        print("Factorial of ",n," is ",x)
    else:
        print("factorial of negative number is not possible")
n=int(input("Enter the num:"))
print(facto(n))
