"""
Native coroutines were introduced in Python 3.5 with PEP 492. They are special functions defined with async def,
and they behave like generators but are specifically designed for asynchronous programming.

Instead of using yield or yield from (like generator-based coroutines did before), native coroutines use:
 * await to suspend execution
 * async def to define a coroutine
 * async for and async with to handle asynchronous iterations and context managers.

Native coroutines are executed in the same thread — usually the main thread —
unless you explicitly move them into another thread.

Native coroutines (async def) work like this:
 * They are scheduled and managed by the event loop.
 * The event loop itself runs inside one thread (usually the main thread).
 * Coroutines yield control (via await) to the event loop, allowing other coroutines to run in the same thread.

 * No new thread is created automatically.
 * No multithreading happens by default.

An event loop is the core object in asynchronous programming (in Python's asyncio and elsewhere).
 * It manages the execution of multiple tasks (coroutines, futures, callbacks)
 * It keeps the program running, and decides when each task is allowed to run.
 * It waits for events (like timers expiring, network replies arriving) and dispatches control to the right coroutine when ready.

"""

# ------
# Basics
# ------
import asyncio

# `async def` defines a native coroutine
async def my_coroutine():
    print("Starting coroutine.")
    await asyncio.sleep(1) # pauses execution without blocking the entire thread.
    print("Coroutine finished.")


# ---------
# async for
# NOTE
#  * When an async for hits an await during __anext__, the whole async for pauses until that await finishes.
#    It does not immediately start the next iteration.
#  * Purpose:
#    * If each item comes asynchronously (e.g., data over network, file chunks),
#      async for lets you wait efficiently without blocking the whole thread.
#    * Between iterations, the event loop can do other things while the current iteration is "waiting."
#    * In normal for, you can't await at all — only async for can await inside the loop header safely.
#    * Streaming data becomes easy and efficient.
# ---------
class AsyncCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        print("Starting next, self.current=" + str(self.current))
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(1)  # Simulate async wait
        print("Finished, self.current=" + str(self.current))
        self.current += 1
        return self.current


# ----------
# async with
#  * Like with, but works with asynchronous context managers.
#  * Useful when opening/closing resources asynchronously (e.g., database connections, websockets).
# ----------
class AsyncResource:
    async def __aenter__(self):
        print("Opening resource")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(1)
        print("Closing resource")



async def main():
    print("Native coroutine - basics\n-----------------------")
    await my_coroutine()

    print("\nasync for\n---------")
    async for number in AsyncCounter(1, 5):
        print(number)

    print("\nasync with\n----------")
    async with AsyncResource() as resource:
        print("Using resource")


if __name__ == "__main__":
    asyncio.run(main())