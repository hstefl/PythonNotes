import tkinter as tk
from pydoc import text

window = tk.Tk()
window.title("Experiment")

label = tk.Label(window, text="Little label: ")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="blue")
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbox = tk.Checkbutton(window, text="Checkbox", variable=switch)
checkbox.pack()

entry = tk.Entry(window, width=30)
entry.pack()

rad1 = tk.Radiobutton(window, text="Salad", variable=switch, value=0)
rad1.pack()
rad2 = tk.Radiobutton(window, text="Pizza", variable=switch, value=1)
rad2.pack()

window.mainloop()