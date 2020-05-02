import random
from helpers import create_end_game_text

ball_size = 15
initial_x_position = 250
initial_y_position = 100

class Ball:
    def __init__(self, canvas, paddle, score, color, speed):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.speed = speed

        self.id = canvas.create_oval(0, 0, ball_size, ball_size, fill=color)

        self.canvas.move(self.id, initial_x_position, initial_y_position)

        possible_initial_x_speed = [-self.speed, self.speed]
        random.shuffle(possible_initial_x_speed)
        self.x = possible_initial_x_speed[0]
        self.y = self.speed

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # [x1, y1, x2, y2]
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = self.speed

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            create_end_game_text(self.canvas)

        if pos[0] <= 0:
            self.x = self.speed

        if pos[2] >= self.canvas_width:
            self.x = -self.speed

        if self.hit_paddle(pos):
            self.y = -self.speed

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True

        return False