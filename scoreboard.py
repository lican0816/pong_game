from turtle import Turtle

FONT = ('Courier', 80, 'normal')
POSITION = 'center'
FONT_COLOR = 'white'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(FONT_COLOR)
        self.penup()  # Do not draw lines when move
        self.hideturtle()  # Do not show default turtle on the screen
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        """
        Show scores on the screen
        """
        self.clear()  # Clear previous scores on the screen
        self.goto(-100, 200)
        self.write(self.l_score, align=POSITION, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=POSITION, font=FONT)

    def increase_l_score(self):
        """
        Increase left side score by 1
        """
        self.l_score += 1
        self.write_score()

    def increase_r_score(self):
        """
        Increase right side score by 1
        """
        self.r_score += 1
        self.write_score()
