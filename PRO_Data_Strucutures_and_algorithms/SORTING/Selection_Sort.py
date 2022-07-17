def selection(A):
    for i in range(len(A)-1,0,-1): # taking length of the list and decrementing by -1
        max_pos = 0
        for j in range(1, i+1):
            if A[j] > A[max_pos]:
                max_pos = j
        temp = A[i]
        A[i] = A[max_pos]
        A[max_pos] = temp

A = [84,21,47,96,15]
print("Original Array: ", A)
selection(A)
print("Sorted Array: ",A)