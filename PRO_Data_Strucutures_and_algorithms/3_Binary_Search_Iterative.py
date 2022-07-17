def binaryS(A,key):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low+high)//2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
A = [20,30,40,50,60]
found = binaryS(A,10)
print("The element 10 is in A: ", found)
