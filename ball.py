import random

ball_size = 15
initial_x_position = 250
initial_y_position = 100

class Ball:
    def __init__(self, canvas, color, speed):
        self.canvas = canvas

        self.speed = speed

        self.id = canvas.create_oval(0, 0, ball_size, ball_size, fill=color)

        self.canvas.move(self.id, initial_x_position, initial_y_position)

        possible_initial_x_speed = [-self.speed, self.speed]
        random.shuffle(possible_initial_x_speed)
        self.x = possible_initial_x_speed[0]
        self.y = self.speed

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()



