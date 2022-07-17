from exceptions import Empty

class ArrayStack:

    def __init__(self):             # CONSTRUCTOR
        self._data=[]

    def __len__(self):              # RETURN LENGTH
        return len(self._data)

    def is_empty(self):             # STACK IS EMPTY OR NOT
        return len(self._data) == 0

    def push(self,e):               # PUSH VALUE IN STACK
        self._data.append(e)

    def pop(self):                  # REMOVE VALUE FROM STACK
        if self.is_empty():
            raise Empty('Stack Is Empty')
        return self._data.pop()

    def top(self):                  # GIVE TOP VALUE
        if self.is_empty():
            raise Empty('Stack Is Empty')
        return self._data[-1]


s = ArrayStack()
s.push(10)
s.push(20)
print('Stack: p', s._data)
print('Length: ', len(s))
print('Is-Empty: ',s.is_empty())
print('Pop: ',s.pop())
print('Stack: ',s._data)

