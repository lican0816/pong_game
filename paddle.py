from turtle import Turtle

# Screen width / 2 - paddle width - margin(30) = 350
POSITION_L = (-350, 0)
POSITION_R = (350, 0)

TOP_DOWN_BOUNDARY = 250  # Screen height / 2 - paddle height / 2 = 250
PADDLE_COLOR = 'white'


class Paddle(Turtle):

    def __init__(self, position, screen):
        super().__init__()
        self.color(PADDLE_COLOR)
        self.penup()  # Do not draw lines when move
        self.shape('square')  # Default size 20 * 20
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch square shape to rectangle, 100 * 20

        screen.listen()  # Listen to key stroke

        if position == 'right':
            self.goto(POSITION_R)
            screen.onkey(self.go_up, 'Q')
            screen.onkey(self.go_down, 'A')

        elif position == 'left':
            self.goto(POSITION_L)
            screen.onkey(self.go_up, 'Up')
            screen.onkey(self.go_down, 'Down')

    def go_up(self):
        """
        Move the paddle up by 20
        """
        new_y = self.ycor() + 20
        if -TOP_DOWN_BOUNDARY <= new_y <= TOP_DOWN_BOUNDARY:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down by 20
        """
        new_y = self.ycor() - 20
        if -TOP_DOWN_BOUNDARY <= new_y <= TOP_DOWN_BOUNDARY:
            self.goto(self.xcor(), new_y)
