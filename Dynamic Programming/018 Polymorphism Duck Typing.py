'''
If there is a bird which looks like a duck,
walks like a duck, swim like a duck, and quacks like a duck
then it probably is a duck.

- If the behaviour of that bird is matching with the duck then its a duck.
'''

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyCharm:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute() # Now the question is the ide is of what type?

ide = PyCharm()      # Type of ide is pychram
'''
We can replace this ide type from PyChram to editor provided we have that method
"execute" to it.

It dosent matter which class object we are passing what matters is that object
should have this "execute" method.
'''

ide = MyCharm()

lap1 = Laptop()
lap1.code(ide)


'''
We Should be having this method execute and thats the case:

If there is a bird which looks like a duck,
walks like a duck, swim like a duck, and quacks like a duck
then it probably is a duck.

In the same way if there is an object ide and it has a method execute 
thats it, we are not concerned which class object it is, what we are concerned 
about "IT SHOULD HAVE THAT METHOD execute" and this is called as duck typing.
'''