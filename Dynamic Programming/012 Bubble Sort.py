def bubbleSort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1], data[j]

data = [1,6,2,4,3,5]
bubbleSort(data)
print(data)