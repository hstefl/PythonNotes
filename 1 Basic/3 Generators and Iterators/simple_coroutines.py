"""
Coroutines in Python are special functions that can pause and resume their execution.

They are like functions, but instead of return, they use yield or await.

You can think of them as functions that remember where they left off.

Use cases:
 1. Pipelines / Streams of Data (iltering, parsing, transforming, or aggregating data streams ...)
 2. Event-driven Programming (a state machine where coroutines respond to events (start, stop, error, etc.).
 3. Cooperative multitasking (If you want lightweight task switching —
    coroutines can yield control back and forth without threads.)
 4. Decouple Producers and Consumers (The producer can send data to the consumer coroutine
    without worrying about how it's processed.)
 5. Customized Control Flows (You can create fancy iteration patterns or advanced generators where
    you feed in values dynamically, pause, checkpoint, retry, etc.)
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