def LinearSearch(data, key):
    for i in range(0,len(data)):
        if data[i]==key:
            return f"{key} present at index {i}"
    return f"{key} not present"

data = [1,2,3,4,5,6,7]
key = 61
x = LinearSearch(data,key)
print(x)