import tkinter as tk
from tkinter import messagebox


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()

