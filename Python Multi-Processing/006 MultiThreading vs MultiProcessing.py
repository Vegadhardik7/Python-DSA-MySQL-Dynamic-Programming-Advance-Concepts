# from threading import Thread
# import math
# import os
#
# def fun():
#     for i in range(0,500000):
#         math.sqrt(i)
#
#
# if __name__ == "__main__":
#
#     threads = []
#
#     for i in range(os.cpu_count()):
#         print(f"registering thread {i}")
#         threads.append(Thread(target=fun))
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
#


from multiprocessing import Process
import math
import os


def fun():
    for i in range(0, 500000):
        math.sqrt(i)


if __name__ == "__main__":

    processes = []

    for i in range(os.cpu_count()):
        print(f"registering thread {i}")
        processes.append(Process(target=fun))

    for t in processes:
        t.start()

    for t in processes:
        t.join()

