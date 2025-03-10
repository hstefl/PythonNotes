"""
Event-driven paradigm
 * event controller
   * detecting, registering and classifying all of a user's actions
 * You have to inform the event controller what you want to perform when a particular event
   (e.g., a mouse click). This is done by writing specialized functions called event handlers.

Flow
 -> Event -> Trigger -> Event handler -> Event loop -> repeat
"""

import tkinter
from tkinter import messagebox


def click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()

skylight = tkinter.Tk() # main window
skylight.title("Skylight")

button = tkinter.Button(skylight, text="Bye!", command=click) # In constructor is specified where to place it
button.place(x=10, y=10)

skylight.mainloop() # start main loop
