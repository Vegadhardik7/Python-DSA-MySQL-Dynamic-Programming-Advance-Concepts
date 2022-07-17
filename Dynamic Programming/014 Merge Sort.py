def MergeSort(data):
    if len(data)>1:
        mid = len(data)//2     # Center value
        left = data[:mid]      # Create Left list
        right = data[mid:]     # Create Right List

        MergeSort(left)
        MergeSort(right)

        i = 0; j = 0; k = 0

        # Mergining 2 sorted list
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i+=1
            else:
                data[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            data[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            data[k] = right[j]
            j+=1
            k+=1

data = [9,5,2,8,7,6,3,1,4]
MergeSort(data)
print(data)