'''
1.) Method Overloading: (Cant do directly in python)
- Let's say we have a class in which we have 2 method with same name
but different parameters it is called as method overloading.

Example:
class Student:
    def average(a,b):
        pass
    def average(a,b,c):
        pass

2.) Method Overriding:
- 2 methods with same name with same number of
parameters in different class

'''

# Method Overloading: (Example)

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s = 0
        if a !=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b !=None:
            s=a+b
        else:
            s=a
        return s

stu = student(4,5)

print(stu.sum(4,5))


# Method Overriding:

class A:
    def show(self):
        print("in A show")
class B(A):
    pass

a1 = B()
a1.show()


class Aclass:
    def show(self):
        print("in Aclass show")
class Bclass(Aclass):
    def show(self):
        print("in Bclass show")

val = Bclass()
val.show()