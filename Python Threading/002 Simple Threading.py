from threading import Thread
import time

class Mythread(Thread):
    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.counter  = counter

    def run(self):
        print('Starting' + self.name)
        print_time(self.name, self.counter, 1)
        print("Exiting", self.name+ "\n")

def print_time(name, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), counter) + "\n")
        counter -= 1

# Create new thread
thread1 = Mythread(1, "Thread-1", 10)
thread2 = Mythread(2, "Thread-2",5)

# Start new Thread
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exit Main Thread")