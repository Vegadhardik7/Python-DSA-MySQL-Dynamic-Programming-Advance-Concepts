def BinarySearch(data, key):
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left+right)//2
        if key < data[mid]:
            right = mid-1
        elif key > data[mid]:
            left = mid+1
        else:
            return True

data = [1,2,3,4,5,6]
x = BinarySearch(data, 1)
print(x)


