from tkinter import Tk, Canvas

window = Tk()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)

#canvas.create_line(10, 10, 100, 100)
#canvas.create_rectangle(150, 50, 100, 90, fill="red")

# head
canvas.create_oval(180, 80, 220, 120)
# body
canvas.create_line(200, 120, 200, 200)
# leg left
canvas.create_line(200, 200, 140, 260)
# leg right
canvas.create_line(200, 200, 260, 260)
# hand left
canvas.create_line(200, 160, 160, 140)
# hand right
canvas.create_line(200, 160, 240, 140)

window.mainloop()
