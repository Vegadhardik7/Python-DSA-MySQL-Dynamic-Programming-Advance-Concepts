# Let's say we have to create a function which only deals with class variables
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

hardik = Employee("Hardik", "Vegad", 50000)
ram = Employee("Ram", "Iyer", 60000)

print("Hardik Salary before :",hardik.salary)
Employee.change_increment(2)                    # Salary will increase 2 times
hardik.increase()
print("Hardik Salary after :",hardik.salary)