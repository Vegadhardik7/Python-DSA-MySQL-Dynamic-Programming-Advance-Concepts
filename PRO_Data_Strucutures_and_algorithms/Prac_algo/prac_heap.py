from exceptions import Empty
class ArrayHeap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1]*self._maxsize  # Initialize all the element of data to be -1
        self._currentsize = 0

    def __len__(self):
        return len(self._data)

    def is_Empty(self):
        return len(self._data)==0

    def maxh(self):
        if self._currentsize==0:
            raise Empty("Heap is Empty")
        return self._data[1]               # Data of 1st element

    def insert(self, e):
        if self._currentsize == self._maxsize:
            raise Empty("No Space")
        self._currentsize += 1
        x = self._currentsize

        # Bubbling Operation below
        while x != 1 and e > self._data[x//2]:
            self._data[x] = self._data[x//2]
            x = x//2
        self._data[x] = e


    def deletemax(self):
        if self._currentsize == self._maxsize:
            raise Empty("No Space")
        x = self._data[1]
        y = self._data[self._currentsize]     # Last element of the heap
        self._currentsize -= 1
        i = 1
        j = 2
        while j < self._currentsize:
            if j < self._currentsize and self._data[j] < self._data[j+1]:
                j += 1
            if y >= self._data[j]:
                break
            # Here we are checking that the last element i.e "y" >= its child : if its greater than the property is satisfied
            self._data[i] = self._data[j]
            i = j
            j = j*2
        self._data[i] = y


h = ArrayHeap()
h.insert(25)
h.insert(14)
h.insert(2)
h.insert(7)
h.insert(6)
h.insert(3)
h.insert(33)
print(h._data)
