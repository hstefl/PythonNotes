import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, arrow=tk.BOTH, fill='red', smooth=True, width=3)
canvas.create_line(200, 10, 380, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)
canvas.create_line(380, 380, 10, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='black')
# canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()
