import tkinter as tk

# Properties handling

def on_off():
    global button
    state = button["text"]
    # state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state
    # button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()
