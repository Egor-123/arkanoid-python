from helpers import create_score_text

initial_score = 0

class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas

        self.score = initial_score

        self.id = create_score_text(canvas, self.score, color)

    def hit(self):
        self.score += 1
        # score = score + 1

        self.canvas.itemconfig(self.id, text=self.score)