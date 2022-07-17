# How to use class method as an alternative constructor
# We use class variable when we don't wanna use attributes of Instance Variable

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

hardik = Employee("Hardik", "Vegad", 50000)

ram = Employee("Ram", "Iyer", 60000)

priya = Employee.from_str("Priya-Aamle-40000") # We want this string to set automatically fname, lname, salary

print(priya.fname, priya.lname, priya.salary)