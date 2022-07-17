# Creating our own iterator
'''
To create our own iterator we has 2 function:
1.)iter:
- Give object of iterator

2.)next:
- Give next object
'''


class TopTen:
    def __init__(self):
        self.cnt = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.cnt <= 10:
            val = self.cnt
            self.cnt+=1
            return val
        else:
            raise StopIteration


values = TopTen()

# Once we wrote this our iterator will continue from 3...
print(values.__next__())
print(next(values))

for i in values:
    print(i)