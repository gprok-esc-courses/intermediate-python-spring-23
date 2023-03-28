from tkinter import Tk, Canvas
from SnakeModel import SnakeModel


# EXERCISE 1: Make fruit appear 10 pixels away from the border
# EXERCISE 2: When snake head hits the border, don't move out of canvas
#             decrease lives, and if lives becomes ZERO, game over.


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
    display_snake()
    canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")


def display_snake():
    for bp in model.body:
        canvas.create_rectangle(bp[0], bp[1], bp[0] + 10, bp[1] + 10, fill="green")


window = Tk()
model = SnakeModel()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)

display_snake()
canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")
window.bind('<KeyRelease>', key_pressed)

window.mainloop()
