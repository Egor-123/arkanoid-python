from tkinter import *
import time

from ball import Ball
from paddle import Paddle
from score import Score

tk = Tk()
tk.title('Арканоид')
tk.resizable(0, 0)

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()

tk.update()

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'black', 2)
ball = Ball(canvas, paddle, score, 'red', 1)
ball2 = Ball(canvas, paddle, score, 'yellow', 1)

while not ball.hit_bottom:

    if paddle.started:
        paddle.draw()
        ball.draw()
        ball2.draw()

    tk.update_idletasks()
    tk.update()

    time.sleep(0.01)

time.sleep(3)