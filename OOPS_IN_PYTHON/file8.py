# Magic / Dunder Method

class Employee:

    # These are class variables
    increment = 1.5
    num_of_emp = 0

    # These are instance variables
    def __init__(self, fname, lname, salary):        # Constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.num_of_emp += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)        # we can also write --> Employee.increment

    # Decorator is used to when we want to take whole class as an argument
    @classmethod         # This is a decorator
    def change_increment(cls, amount):
        cls.increment = amount

    # This will work as an alternative constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")  # Split String by "-"
        return cls(fname, lname, salary)

    # This do not take Class as an argument and nor self
    @staticmethod
    def is_open(day):
        if day == "Sunday":
            return False
        else:
            return True

    # Dunder Method
    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return "Employee({},{},{})".format(self.fname,self.lname,self.salary)

    def __str__(self):
        return "The Full name of the employee is {} {}".format(self.fname,self.lname)



ria = Employee("Ria", "Jain", 30000)
hardik = Employee("Hardik","Vegad",30000)
print(hardik+ria)
print(hardik)
print(repr(hardik))