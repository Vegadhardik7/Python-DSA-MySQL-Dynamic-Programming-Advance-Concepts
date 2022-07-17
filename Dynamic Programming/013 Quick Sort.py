def QuickSort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        QuickSort(data, low, p-1)
        QuickSort(data, p+1, high)

def partition(data, low, high):
    i = low-1
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return i+1 # returning pivot value

data = [9,5,2,8,7,6,3,1]
QuickSort(data,0,len(data)-1)
print(data)