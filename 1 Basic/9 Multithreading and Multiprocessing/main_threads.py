#
# Multithreading in Python
#
# Overview
#   Multithreading is a technique where multiple threads are spawned by a process to execute tasks concurrently.
#   Python's Global Interpreter Lock (GIL) can be a limitation for CPU-bound tasks,
#   but it works well for I/O-bound tasks.
#
# Key Concepts
#  * Thread: The smallest unit of a process, responsible for executing code.
#  * GIL (Global Interpreter Lock): A mutex that protects access to Python objects,
#    preventing multiple native threads from executing Python bytecodes simultaneously.
#
# Libraries
#   Threading module
#
# More about threads
#   Thread: A thread is the smallest unit of execution within a process. It is often referred to as a
#   "lightweight process."
#
# Characteristics:
#   Shared Memory: Threads within the same process share the same memory space.
#   Context: Each thread has its own stack, registers, and program counter, but shares code, data, and open
#     files with other threads in the same process.
#   Concurrency: Threads enable concurrent execution within the same process.
#
# Key Components
#   TID (Thread Identifier): A unique identifier for each thread.
#   Shared Resources: Threads share global variables, file descriptors, etc.
#   Synchronization: Mechanisms like locks, semaphores, and condition variables are used to manage access to
#   shared resources.
#
# Use Cases
#   I/O-bound Tasks: Suitable for tasks that spend a lot of time waiting for I/O operations.
#   Shared Data: Ideal when tasks need to share data frequently.
#


import threading
from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers():
    for i in range(10):
        time.sleep(0.1)
        print(i)


def print_letters():
    for c in "abcdefgh":
        time.sleep(0.2)
        print(c)


def task(n):
    return n * n


def main():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("thread1 and thread2 finished")

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(task, range(10))
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
