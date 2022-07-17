import threading
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

for _ in range(2):
    x = threading.Thread(target=count, args=(10,)) # (10,) or it will consider 10
    x.start()

print("\n- YOU PAUSED FOR 0.01 SEC, SO I GOT EXECUTED -")