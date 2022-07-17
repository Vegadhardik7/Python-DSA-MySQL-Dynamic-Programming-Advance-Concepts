def prime(n):
    if(n>1):
        for i in range(2,n//2):
            if n%i==0:
                print(n," is not a prime number")
                break
        else:
            print(n," is a prime number")
    else:
        print(n," is not a prime number")
n=int(input("Enter the number:"))
print(prime(n))
