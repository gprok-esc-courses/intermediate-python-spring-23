import tkinter as tk


def button_command():
    txt = field.get()
    print(txt)
    label.configure(text=txt)


window = tk.Tk()

label = tk.Label(text="Hello World")
label.pack()

field = tk.Entry()
field.pack()

btn = tk.Button(text="Click me", command=button_command)
btn.pack()

window.mainloop()
