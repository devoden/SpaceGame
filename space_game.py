from tkinter import *
from random import *


root = Tk()
root.title("Охота на пришельцев")
root.geometry('800x500+0+0')
root.config(bg='black')

canvas = Canvas(root)
canvas.config(width=800, height=500, bg='black')
canvas.pack()

n = 1000
for k in range(n):
    x = randint(0, 795)
    y = randint(0, 495)
    canvas.create_oval(x, y, x + 1, y + 1, outline='white', fill='white')

shuttle1_img = PhotoImage(file='shuttle1.png')
shuttle1_img = shuttle1_img.subsample(4, 4)
shuttle1 = canvas.create_image(300, 50, image=shuttle1_img, anchor=NW)


def move_control(event):
    ascii_code = event.keycode
    # print(ascii_code)
    d = 5
    if ascii_code == 37:
        canvas.move(shuttle1, -d, 0)
    elif ascii_code == 39:
        canvas.move(shuttle1, d, 0)
    elif ascii_code == 38:
        canvas.move(shuttle1, 0, -d)
    elif ascii_code == 40:
        canvas.move(shuttle1, 0, d)


canvas.bind('<Key>', move_control)
canvas.focus_set()
root.mainloop()
