import tkinter as tk

user = "X"


def play(event):
    global user
    btn = event.widget
    btn.configure(text=user)
    # btn['state'] = "disabled"
    btn.unbind("<Button-1>")
    user = "X" if user == "O" else "O"


window = tk.Tk()
window.title("TicTacToe")

frame = tk.Frame(master=window)

buttons = []

for i in range(3):
    buttons_row = []
    for j in range(3):
        b = tk.Button(master=frame, text="-")
        b.bind('<Button-1>', lambda event: play(event))
        b.grid(row=i, column=j)
        buttons_row.append(b)
    buttons.append(buttons_row)

frame.pack()

window.mainloop()
