def insertionSort(data):
    for i in range(1,len(data)):
        pos = i
        val = data[i]
        while pos > 0 and data[pos-1]>val:
            data[pos] = data[pos-1]
            pos = pos-1
        data[pos] = val

data = [10,12,31,4]
print("Original Data:",data)
insertionSort(data)
print("Sorted Data:",data)