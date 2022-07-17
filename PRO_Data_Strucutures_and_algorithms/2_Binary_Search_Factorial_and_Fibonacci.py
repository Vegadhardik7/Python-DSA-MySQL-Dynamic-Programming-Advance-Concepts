# FACTORIAL
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 5 is : ", fact)

print("---------------------------------------------------------------------")

# FIBONACCI SERIES

nterms = 10

# first two terms
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < nterms:
   print(n1)
   nth = n1 + n2
   # update values
   n1 = n2
   n2 = nth
   count += 1
