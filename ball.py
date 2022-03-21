from turtle import Turtle

BALL_MOVE_SPEED = 10  # Distance the ball moves each time
SIDE_BOUNDARY = 350  # Screen width / 2 - paddle width - margin(30) = 350
TOP_DOWN_BOUNDARY = 280  # Screen height / 2 - ball size = 280
BALL_COLOR = 'blue'
BALL_SHAPE = 'circle'


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.penup()  # Do not draw lines when move
        self.shape(BALL_SHAPE)  # Default size 20 * 20

        # Default the ball to move to top right corner, see move() for details
        self.move_direction_y = 1
        self.move_direction_x = 1

    def move(self):
        """
        Move the ball according to default speed and direction
        """
        new_y = self.ycor() + BALL_MOVE_SPEED * self.move_direction_y
        new_x = self.xcor() + BALL_MOVE_SPEED * self.move_direction_x
        self.goto(new_x, new_y)

    def bounce_wall(self):
        """
        Bounce the ball if it hits the walls
        """
        if self.ycor() >= TOP_DOWN_BOUNDARY or self.ycor() <= -TOP_DOWN_BOUNDARY:
            self.move_direction_y *= -1

    def bounce_paddles(self, *paddles):
        """
        Bounce the ball if it hits the paddles
        """
        for paddle in paddles:
            # 325 and 55 is based on testing
            # If greater than 325, the ball may get into the paddle
            # If greater than 55, the ball may bounce before reaching the paddle
            if (self.xcor() >= 325 or self.xcor() <= -325) and self.distance(paddle) < 55:
                self.move_direction_x *= -1

    def l_paddle_miss(self):
        """
        Check if the left paddle miss the ball
        """
        if self.xcor() <= -SIDE_BOUNDARY:
            self.reset_position()
            return True

    def r_paddle_miss(self):
        """
        Check if the right paddle miss the ball
        """
        if self.xcor() >= SIDE_BOUNDARY:
            self.reset_position()
            return True

    def reset_position(self):
        """
        The ball goes back to the default position and start to move to the opposite direction
        """
        self.goto(0, 0)
        self.move_direction_x *= -1
