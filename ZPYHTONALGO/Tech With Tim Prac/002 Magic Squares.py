numbers = int(input())
matrix = []

for row in range(numbers):          # Number of rows
    nums = input()                  # Input in that row
    matrix.append([int(x) for x in nums.split()]) # Having [[],[],[]...]

magic = True

cMAtrix = [[] for x in range(numbers)]
value = sum(matrix[0])

'''
We can take a 3 step approch:
- Rows must add
- Columns must add
- Diagonals must add 
'''

# Row:
for x, row in enumerate(matrix):
    if sum(row) != value:
        magic = False

    for y, element in enumerate(row):
        cMAtrix[y].append(element)

# Columns
for x, column in enumerate(cMAtrix):
    if sum(column) != value:
        magic = False

# Diagonals
i=0
j=0
diagonals = [[],[]]
for x in range(numbers):
    diagonals[0].append(matrix[i][j])
    diagonals[1].append(matrix[numbers-1-i][j])
    i+=1
    j+=1

if sum(diagonals[0])!=value or sum(diagonals[1])!=value:
    magic=False

if magic == True:
    print("Magic")
else:
    print("Not Magic")
