from exceptions import Empty
class CricularLinkedList:
    class _Node:
        __slots__ = "_element", "_next"

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

    def add_first(self, e):
        newest = self._Node(e,None)
        if self.is_Empty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self, e):
        newest = self._Node(e,None)
        if self.is_Empty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self._Node(e,None)
        thead = self._head
        i = 1
        while i < pos:
            thead = thead._next
            i += 1
        newest._next = thead._next
        thead._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_Empty():
            raise Empty('List is Empty')
        else:
            oldhead = self._tail._next
            self._tail._next = oldhead._next
            oldhead._next = self._head
            self._size -= 1
            if self.is_Empty():
                self._tail = None
            return oldhead._element

    def remove_last(self):
        if self.is_Empty():
            raise Empty('List is Empty')
        thead = self._head
        i = 0
        while i < len(self)-2:
            thead = thead._next
            i+=1
        self._tail._next = self._head
        self._tail = thead
        thead = thead._next
        val = thead._element
        self._size -= 1
        return val

    def remove_any(self, pos):
        if self.is_Empty():
            raise Empty('List is Empty')
        thead = self._head
        i = 0
        while i < pos-1:
            thead = thead._next
            i += 1
        val = thead._next._element
        thead._next = thead._next._next
        self._size -= 1
        return val

    def display(self):
        thead = self._head
        i = 0
        while i < len(self):
            print(thead._element, end="->")
            thead = thead._next
            i += 1
        print()

lst = CricularLinkedList()
lst.add_first(10)
lst.display()
lst.add_first(12)
lst.display()
lst.add_first(15)
lst.display()
lst.add_first(17)
lst.display()
lst.add_last(20)
lst.display()
lst.add_any(30,2)
lst.display()

lst.remove_first()
lst.display()
lst.remove_last()
lst.display()

lst.remove_any(1)
lst.display()

lst.add_last(99)
lst.display()