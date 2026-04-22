import turtle

import random

import time

screen = turtle.Screen()

screen.title("Racer Game")

screen.bgcolor("black")

screen.setup(width=600, height=600)

screen.tracer(0)

# Player car

car = turtle.Turtle()

car.shape("square")

car.color("blue")

car.penup()

car.goto(0, -250)

# Coin

coin = turtle.Turtle()

coin.shape("circle")

coin.color("yellow")

coin.penup()

coin.goto(random.randint(-250, 250), 250)

score = 0

# Score display

pen = turtle.Turtle()

pen.hideturtle()

pen.color("white")

pen.penup()

pen.goto(0, 260)

pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))


# Controls

def left():
    x = car.xcor()

    if x > -250:
        car.setx(x - 30)


def right():
    x = car.xcor()

    if x < 250:
        car.setx(x + 30)


screen.listen()

screen.onkey(left, "Left")

screen.onkey(right, "Right")

# Game loop

while True:

    screen.update()

    # move coin down

    y = coin.ycor()

    coin.sety(y - 5)

    # reset coin

    if coin.ycor() < -300:
        coin.goto(random.randint(-250, 250), 250)

    # collision

    if car.distance(coin) < 20:
        score += 1

        pen.clear()

        pen.write(f"Score: {score}", align="center", font=("Arial", 16))

        coin.goto(random.randint(-250, 250), 250)

    time.sleep(0.05)
