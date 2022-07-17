# Property Decorators, Setters & Deleters

class Employee:
    # These are class variables
    increment = 1.5
    num_of_emp = 0

    # These are instance variables
    def __init__(self, fname, lname, salary):  # Constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.num_of_emp += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)  # we can also write --> Employee.increment

    @property
    def email(self):
        if self.lname == None:
            return "Email Not set"
        else:
            return self.fname + '.' +self.lname + "@gmail.com"

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


    # Decorator is used to when we want to take whole class as an argument
    @classmethod  # This is a decorator
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

if __name__== "__main__":
    ria = Employee("Ria", "Jain", 30000)
    hardik = Employee("Hardik", "Vegad", 30000)
    print(ria.email, hardik.email)
    ria.lname = "Sharma"
    print(ria.email)
    ria.email = "Sharma.Ria@gmail.com"
    print(ria.email)
    del ria.email
    print(ria.email)