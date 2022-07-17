import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping in {seconds} Seconds...")
    time.sleep(seconds)
    return "Done Sleeping..."


if __name__ == '__main__':

    # Encapsulates the execution of the function and allows us to check on it after it's been scheduled.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 1)
        print(f1.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2 )} second(s)')


'''
                       1 Second
Process2              ^       |
                      |       |
                  func()      |
                       1 Second
Process1              ^       |
                      |       |
                  func()      |
                              v
                             Done

------------------------- TIME ----------------------->

'''