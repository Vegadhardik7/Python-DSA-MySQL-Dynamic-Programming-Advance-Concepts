class getKSmallestLargest:
    def __init__(self,data):
        self.data = data
    def getKLargest(self,k):
        value = sorted(self.data)
        print(value)
        print(f"{k} largest element in the list is {value[-k]}")
    def getKSmallest(self,k):
        value = sorted(self.data)
        print(value)
        print(f"{k} smallest element in the list is {value[k]}")

data = [1,5,2,3,4]

values = getKSmallestLargest(data)

larget = values.getKLargest(2)
print(larget)

smallest = values.getKSmallest(1)
print(smallest)














