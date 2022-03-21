from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_COLOR = 'black'
SCREEN_TITLE = 'Pong Game'

"""
--------------------- Game Setup ---------------------
"""

# Setup screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)  # Turn off animation

# Setup paddles
paddleR = Paddle('right', screen)
paddleL = Paddle('left', screen)

ball = Ball()  # Setup Ball

scoreboard = Scoreboard()  # Setup scoreboard

"""
--------------------- Game Start ---------------------
"""
game_on = True


def game_over():
    global game_on

    game_on = False


while game_on:
    time.sleep(0.1)  # Control speed of the game
    screen.update()  # Refresh the screen
    ball.move()
    ball.bounce_wall()
    ball.bounce_paddles(paddleL, paddleR)

    if ball.l_paddle_miss():
        scoreboard.increase_r_score()
    if ball.r_paddle_miss():
        scoreboard.increase_l_score()

screen.exitonclick()  # Keep the screen on
