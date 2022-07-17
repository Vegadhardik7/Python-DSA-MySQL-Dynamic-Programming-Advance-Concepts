import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping in {seconds} Seconds...")
    time.sleep(seconds)
    return f"Done Sleeping... {seconds}"


if __name__ == '__main__':

    # Encapsulates the execution of the function and allows us to check on it after it's been scheduled.
    # ProcessPoolExecutor based on hardware allot the processes
    with concurrent.futures.ProcessPoolExecutor() as executor:

        secs = [5,4,3,2,1]

        # Process will be returned
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} second(s)')


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