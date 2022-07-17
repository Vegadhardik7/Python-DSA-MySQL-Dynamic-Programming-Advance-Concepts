def countOccurance(data, key):
    res = 0
    value = []
    for i in range(len(data)):
        if key == data[i]:
            res+=1
            value.append(i)
    return f"Count of {key} is {res} at index {value}"

lst = [1,2,3,4,4,5,5,0,1,6,6,2,2,2,1]
x = countOccurance(lst, 1)
print(x)
