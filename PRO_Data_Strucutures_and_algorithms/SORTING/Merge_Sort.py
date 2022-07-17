def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        # This while loop is use to merge the 2 sorted list into 1 single sorted list
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i +=1
            else:
                A[k] = right[j]
                j +=1
            k +=1

        while i < len(left):
            A[k] = left[i]
            i +=1
            k +=1
        while j<len(right):
            A[k] = right[j]
            j +=1
            k +=1
A=[84,6,45,32,88]
print("Before Merge Sort:",A)
merge_sort(A)
print("After Merge Sort:",A)


