import multiprocessing
import time

start = time.perf_counter()

def do_something():
    print("Sleeping in 1 Second...")
    time.sleep(1)
    print("Done Sleeping")


if __name__ == '__main__':

    processes = []

    # _ : Throw away variable
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

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