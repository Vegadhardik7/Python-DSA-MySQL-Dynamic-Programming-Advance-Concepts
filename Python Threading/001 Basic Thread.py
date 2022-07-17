import threading
import time

def fun():
    print("Run"+"\n")
    time.sleep(1)
    print("Done")
    time.sleep(1)
    print("Now Done")
x = threading.Thread(target = fun)

# Run thread
x.start()
print(threading.activeCount())
time.sleep(1)
print("Finally")
print()
