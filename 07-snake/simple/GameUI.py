from tkinter import Tk, Canvas
from Model import Model


def key_pressed(e):
    key = e.keysym
    if key == "Down":
        model.move_down()
    elif key == "Up":
        model.move_up()
    elif key == "Left":
        model.move_left()
    elif key == "Right":
        model.move_right()
    canvas.delete("all")
    canvas.create_rectangle(model.x, model.y, model.x + 10, model.y + 10, fill="green")


window = Tk()
model = Model()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)

canvas.create_rectangle(model.x, model.y, model.x+10, model.y+10, fill="green")
window.bind('<KeyRelease>', key_pressed)

window.mainloop()
