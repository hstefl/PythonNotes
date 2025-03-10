#
# Multiprocessing in Python
#
# Overview
#   Multiprocessing involves multiple processes running independently, each with its own Python
#   interpreter and memory space.
#   It bypasses the GIL, making it suitable for CPU-bound tasks.
#
# Key Concepts
#  * Process: An independent unit of execution with its own memory space.
#  * Inter-process Communication (IPC): Mechanisms like queues and pipes to exchange data between processes.
#
# Libraries
#   multiprocessing module
#
# Use Cases
#  CPU-bound tasks like data processing, scientific computations, rendering
#
# IPC Mechanisms
#   Queue: A thread and process-safe queue class.
#   Pipe: A two-way communication channel between processes.
#
# -----------------------------------------------------------------
#
# More about process
#   A process is an instance of a program in execution. It is the fundamental unit of computation that the operating
#   system manages.
#
# Characteristics:
#   Independent Execution: Each process runs independently and is isolated from other processes.
#   Memory Space: Each process has its own memory space, which includes its code, data, and system resources.
#   Context: A process has its own context, including registers, stack, and program counter.
#   Lifecycle: Processes go through various states like new, ready, running, waiting, and terminated.
#
# Key Components
#   PID (Process Identifier): A unique identifier assigned to each process by the operating system.
#   Memory: Divided into segments (text, data, stack, heap).
#   File Descriptors: Handles to resources like files, sockets, etc.
#
# Use Cases
#   Heavy Computations: Suitable for CPU-bound tasks.
#   Isolation: Ideal when tasks need to be isolated to prevent data corruption.

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
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
    # Create processes
    proc1 = multiprocessing.Process(target=print_numbers)
    proc2 = multiprocessing.Process(target=print_letters)

    # Start processes
    proc1.start()
    proc2.start()

    # Wait until the process terminates
    proc1.join()
    proc2.join()

    print("Proc1 and proc2 finished")

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(task, range(10))
        for result in results:
            print(result)


if __name__ == "__main__":
    main()

