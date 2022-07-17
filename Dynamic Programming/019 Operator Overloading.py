'''
Overloading: Have Same method name but arguments or type of
arguments are different

example: + can be used in int, float, string...etc

Operator remains same but operands will change

5+6
 5 & 6 } Operands
    +  } Operator

    int.__add__(5,6)
'''

class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # "Overloading Operators"
    def __add__(self, other): # stu1,stu2
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Students(m1,m2)

        return s3

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s4 = Students(m1,m2)

        return s4

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.m1}, {self.m2}"

'''
If you add 2 different operands we have to overload that operator
'''
stu1 = Students(60,62)
stu2 = Students(55,60)

value1 = stu1 + stu2

'''
    Stu1 | Stu2
    50   |  62
    45   |  60
    _____|_____
    95      122
'''
print(value1.m1)
print(value1.m2)

print('-'*10)

value2 = stu1-stu2

'''
    Stu1 | Stu2
    50   |  62
    45   |  60
    _____|_____
    5        2
'''
print(value2.m1)
print(value2.m2)

print('-'*10)

if stu1 > stu2:
    print("stu1 wins!!!")
else:
    print("stu2 wins!!!")


'''
If you want to perform any operation on the objects 
which are user defined we have to use operator overloading
'''
print("-"*10)
print(stu1)
print(stu2)













