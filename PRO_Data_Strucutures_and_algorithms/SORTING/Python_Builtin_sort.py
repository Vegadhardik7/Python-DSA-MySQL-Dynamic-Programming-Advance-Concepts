A = [84,12,45,22,89]

print("Original List A:",A)
A.sort()
print("Sorted A:",A)

print("---------------------------------------------------")

X = [8,5,45,2,89]
print("Original List X:",X)
B = sorted(X)
print("Sorted List:",B)

print("---------------------------------------------------")

Y = [18,2,45,12,8]
print("Original List Y:",Y)
Y.sort(reverse=True)
print("Reverse Sorted List:",Y)


print("---------------------------------------------------")

colors = ['red','green','blue','white']
print("Original List colors:",colors)
colors.sort()
print("Sorted List:",colors)
colors.sort(reverse=True)
print("Reverse Sorted List:",colors)
colors.sort(key=len)
print("Sorted by length:",colors)