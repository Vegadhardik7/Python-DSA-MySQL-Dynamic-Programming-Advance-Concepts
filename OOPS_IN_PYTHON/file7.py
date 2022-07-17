# Inheritance

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

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname,lname,salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
        self.salary = int(self.salary * (self.increment+0.2))        # we can also write --> Employee.increment
        return self.salary

hardik = Programmer("Hardik", "Vegad", 99000, "Python", "5 years")
print(hardik.fname)
print(hardik.increase())