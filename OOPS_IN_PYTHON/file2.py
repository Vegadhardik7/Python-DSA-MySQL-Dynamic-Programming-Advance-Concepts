class Employee:
    def __init__(self, fname, lname, salary):        # Constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary

hardik = Employee("Hardik", "Vegad", 50000)
ram = Employee("Ram", "Iyer", 60000)

print(hardik.salary,ram.salary)