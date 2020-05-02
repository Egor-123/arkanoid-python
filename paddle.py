import random

initial_speed = 0
position_over_bottom = 50
possible_starting_positions = [40, 60, 90, 120, 150, 180, 200]

paddle_width = 100
paddle_height = 10

right_arrow = '<KeyPress-Right>'
left_arrow = '<KeyPress-Left>'
return_button = '<KeyPress-Return>'

class Paddle:
    def __init__(self, canvas, color, speed):
        self.canvas = canvas

        self.id = canvas.create_rectangle(
            0, 0,
            paddle_width, paddle_height,
            fill=color
        )

        random.shuffle(possible_starting_positions)
        self.starting_point_x = possible_starting_positions[0]

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        self.canvas.move(
            self.id,
            self.starting_point_x,
            self.canvas_height - position_over_bottom
        )

        self.x = initial_speed

        self.speed = speed

        self.canvas.bind_all(right_arrow, self.turn_right)
        self.canvas.bind_all(left_arrow, self.turn_left)
        self.canvas.bind_all(return_button, self.start_game)

        self.started = False

    def turn_right(self, event):
        self.x = self.speed

    def turn_left(self, event):
        self.x = -self.speed

    def start_game(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        # [x1, y1, x2, y2]
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0

        if pos[2] >= self.canvas_width:
            self.x = 0