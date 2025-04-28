"""
Coroutines in Python are special functions that can pause and resume their execution.

They are like functions, but instead of return, they use yield or await.

You can think of them as functions that remember where they left off.
"""

"""
When you call simple_coroutine(), nothing really runs yet.
You have to next() it to start.
Then it pauses at yield.
You can then send it a value.
"""
def simple_sub_coroutine():
    print("[Sub] Sub-coroutine started")
    while True:
        x = yield
        print(f"[Sub] Received: {x}")

def simple_main_coroutine():
    print("[Main] Main coroutine started")
    yield from simple_sub_coroutine()
    print("[Main] Main coroutine done")

def main():
    coro = simple_main_coroutine()  # Nothing printed yet
    next(coro)                 # Prints "Coroutine started"
    coro.send(42)              # Prints "Received: 42"
    coro.send(100)
    coro.close()


if __name__ == "__main__":
    main()