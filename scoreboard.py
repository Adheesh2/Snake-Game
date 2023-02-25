from turtle import Turtle

ALIGN = "center"
FONT = ('Courier', 17, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!!", align=ALIGN, font=FONT)

    def display_score(self):
        self.clear()
        self.write(f"Your Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()
