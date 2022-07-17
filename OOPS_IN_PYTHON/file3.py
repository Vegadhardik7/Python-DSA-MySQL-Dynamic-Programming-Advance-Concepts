# In this we will create a class variable which will be common for all the Employee

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

print("Number of Employee before :",Employee.num_of_emp)

hardik = Employee("Hardik", "Vegad", 50000)
ram = Employee("Ram", "Iyer", 60000)

print("Number of Employee After :",Employee.num_of_emp)

print("-------------------------------------------------------")

# To see all the variables in instance i.e def __init__(...)
print("variables in instance i.e def __init__(...) :")
print(hardik.__dict__)

print("-------------------------------------------------------")

print("Before Increase in salary:",hardik.salary,ram.salary)
hardik.increase()
print("After Increase in salary:",hardik.salary,ram.salary)

