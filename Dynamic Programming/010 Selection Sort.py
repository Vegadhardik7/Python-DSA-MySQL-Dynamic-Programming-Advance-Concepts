def SelectionSort(data):
    for i in range(len(data)-1,0,-1):
        max_pos = 0
        for j in range(1,i+1):
            if data[j] > data[max_pos]:
                max_pos = j
        data[i],data[max_pos] = data[max_pos],data[i]

data = [1,5,2,3,4]
SelectionSort(data)
print(data)