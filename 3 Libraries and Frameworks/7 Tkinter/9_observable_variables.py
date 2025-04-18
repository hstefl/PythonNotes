"""
You can only create an observable variable after the main window initialization.

There are four kinds (types) of observable variable used by tkinter:
    BooleanVar
    DoubleVar
    IntVar
    StringVar

s = StringVar()
s.set("To be or not to be")
sn = s.get()
"""

import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()  # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + 'f')
print(variable.get())
