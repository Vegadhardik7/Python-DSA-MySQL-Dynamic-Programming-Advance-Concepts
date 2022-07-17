from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for j in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()  # When we call start, it will internally call the hellorun method
sleep(0.2)
t2.start()  # When we call start, it will internally call the hirun method

# Hey, Main Thread please continue after t1 and t2 joins
t1.join()
t2.join()

print("Bye")