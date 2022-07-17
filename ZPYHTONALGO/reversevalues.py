n=int(input("Enter the number:"))
r=0
num=n
while num!=0:
    x=num%10
    r=r*10+x
    num=num//10
print(r)
