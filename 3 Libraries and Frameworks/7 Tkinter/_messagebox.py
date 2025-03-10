import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()
