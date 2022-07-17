def printFirstRepeating(data, n):
    mininum = -1
    myset = dict()

    for i in range(n-1,-1,-1):
        if data[i] in myset.keys():
            mininum = i
        else:
            myset[data[i]] = 1
    if (mininum != -1):
        print("The First Repeating Element is ",data[mininum])
    else:
        print("There are no repeating elements")

lst = [11,2,3,4,5,1,2,4]

n = len(lst)

x = printFirstRepeating(lst,n)
print(x)


