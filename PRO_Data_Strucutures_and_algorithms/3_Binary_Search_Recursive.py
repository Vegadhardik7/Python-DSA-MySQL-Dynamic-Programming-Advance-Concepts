def binaryS(A,key,low,high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key < A[mid]:
            return binaryS(A,key,low,mid-1)
        elif key > A[mid]:
            return binaryS(A,key,mid+1,high)
        else:
            return True

A = [20,30,40,50,60,]
found = binaryS(A,50,0,5)
print("The element 50 in A:",found)