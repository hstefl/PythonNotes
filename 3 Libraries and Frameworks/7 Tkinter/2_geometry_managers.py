"""
Geometry managers
 * Three different methods to place widget.

1. Place is the most detailed one. It forces you to precisely declare a widget's location, pixel by pixel. It won't, however, protect you from some common mistakes causing the widgets to overlap each other
or to place some of them, partially or fully, outside the window.
2. "Pack" geometry manager.
3. "Grid" geometry manager.

These managers cannot be mixed.
"""

import tkinter as tk

# Place method - method place specify x,y
# ---------------
window1 = tk.Tk()
button_1 = tk.Button(window1, text="Button #1")
button_2 = tk.Button(window1, text="Button #2")
button_3 = tk.Button(window1, text="Button #3")
button_1.place(x=10, y=10)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70)
window1.mainloop()

# Place method - method grid specifies row and column
# ---------------
window2 = tk.Tk()
button_1 = tk.Button(window2, text="Button #1")
button_2 = tk.Button(window2, text="Button #2")
button_3 = tk.Button(window2, text="Button #3")
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=2)
window2.mainloop()

# Place method - method pack
# ---------------
window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()