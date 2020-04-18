from tkinter import *

from ball import Ball

tk = Tk()
tk.title('Арканоид')
tk.resizable(0, 0)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()

ball = Ball(canvas, 'red', 2)

tk.update()

tk.mainloop()