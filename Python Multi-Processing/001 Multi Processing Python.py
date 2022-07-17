import time

start = time.perf_counter()

def do_something():
    print("Sleeping in 1 Second...")
    time.sleep(1)
    print("Done Sleeping")

do_something()
do_something() # Before calling this our scrip do nothing but just sleep for 1 second

finish = time.perf_counter()

print(f"Finish in {round(finish-start,2)}, second(s)")

'''
******** Running Task Synchronously **********

            1 second             1 second
           |         |          |         |
do_something         do_something         Done

------------------- TIME ----------------------->

If we not want to run our task Synchronously then we can use mutiprocessing
'''