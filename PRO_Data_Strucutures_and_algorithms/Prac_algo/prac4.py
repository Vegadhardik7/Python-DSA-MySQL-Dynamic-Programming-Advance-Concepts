# creating Queue using Linked List
from exceptions import Empty
class QueueLinkekList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_Empty(self):
        return self._size == 0

    def enqueue(self,e):
        newest = self._Node(e,None)
        if self.is_Empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_Empty():
            return Empty('Queue is Empty')
        val = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_Empty():
            self._tail = None
        return val

    def first(self):
        if self.is_Empty():
            return Empty('Queue is Empty')
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element,end='-->')
            temp = temp._next
        print()

lq = QueueLinkekList()
lq.enqueue(10)
lq.display()
lq.enqueue(20)
lq.display()
lq.enqueue(30)
lq.display()

lq.dequeue()
lq.display()

