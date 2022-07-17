'''
                                Checkout
                                   |
                   |---------------|-----------------|
                Payment          Send             Load
                Process       Conformation      Thank You
                                Email             Page

- While Payment Process is happening load other page in background.
(We will be locking the thread untill its done and release it when it is finished)
'''

import threading
import time

class Mythread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.counter  = counter

    # Only when it's done with thread-1 than it will jump on thread-2
    def run(self):
        print('Starting' + self.name + "\n")
        threadLock.acquire()
        print_time(self.name, self.counter, 1)
        threadLock.release()
        print("Exiting", self.name+ "\n")

def print_time(name, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), counter) + "\n")
        counter -= 1

threadLock = threading.Lock()

# Create new thread
thread1 = Mythread(1, "Thread-1", 10)
thread2 = Mythread(2, "Thread-2",5)

# Start new Thread
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exit Main Thread")














