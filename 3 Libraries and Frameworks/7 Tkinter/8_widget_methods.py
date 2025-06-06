"""

after() – this method expects two arguments:
the first is a time interval specification (expressed in milliseconds: 1 s = 1000 ms) and
the second points to an existing function; successful invocation of the method causes the event manager to change its plans;
when the number of milliseconds elapses, the manager will invoke the function (only once);
note: this the only possible way of controlling the passage of time when using an event-driven environment.

Why? Because you can’t just invoke the built-in sleep() function within any of your callbacks – it would freeze your application for the whole nap time; the after() method returns a value which is as specific as the method itself – it’s a unique id of the planned invocation; is it usable? Yes, it is, e.g., when you are going to delete the previously planned invocation from the manager’s calendar, which is done with a method named…

after_cancel(id) – the method cancels the planned invocation identified by the id argument.

"""

import tkinter as tk


def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)


is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)
frame.pack()
window.mainloop()
