def linearsearch(A,key):
    position = 0
    flag = False      # This variable will be used to check whether we have found the key or not
    while position <= len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            position = position+1
    return flag


A=[80,21,30,60]
found = linearsearch(A,21)
print("Element 21 is present in A:",found)