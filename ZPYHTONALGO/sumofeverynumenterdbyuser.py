n=int(input("Enter the number:"))
result=0
while n!=0:
    digit=n%10
    result=result+digit
    n=n//10
print("Additon of all the number is:",result)
