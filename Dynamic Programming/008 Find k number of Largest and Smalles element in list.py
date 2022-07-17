def Klargest(data, k):
    data.sort(reverse=True)

    for i in range(k):
        print(data[i], end=" ")


def KSmallest(data, k):
    data.sort(reverse=False)

    for i in range(k):
        print(data[i], end=" ")

data = [1,22,4,5,99,34]
k = 2
x = Klargest(data,k)
print(x)

y = KSmallest(data,k)
print(y)