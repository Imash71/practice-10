import turtle

import random

import time

screen = turtle.Screen()

screen.title("Snake")

screen.bgcolor("black")

screen.setup(600, 600)

screen.tracer(0)

head = turtle.Turtle()

head.shape("square")

head.color("green")

head.penup()

head.goto(0, 0)

head.direction = "stop"

food = turtle.Turtle()

food.shape("circle")

food.color("red")

food.penup()

food.goto(0, 100)

segments = []

score = 0

level = 1

delay = 0.15

pen = turtle.Turtle()

pen.hideturtle()

pen.color("white")

pen.penup()

pen.goto(0, 260)

pen.write("Score: 0 Level: 1", align="center")


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


screen.listen()

screen.onkey(go_up, "Up")

screen.onkey(go_down, "Down")

screen.onkey(go_left, "Left")

screen.onkey(go_right, "Right")

while True:

    screen.update()

    # границы

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:

        head.goto(0, 0)

        head.direction = "stop"

        score = 0

        level = 1

        delay = 0.15

        for s in segments:
            s.goto(1000, 1000)

        segments.clear()

    # еда

    if head.distance(food) < 20:

        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new = turtle.Turtle()

        new.shape("square")

        new.color("green")

        new.penup()

        segments.append(new)

        score += 1

        if score % 3 == 0:
            level += 1

            delay *= 0.8

        pen.clear()

        pen.write(f"Score: {score} Level: {level}", align="center")

    # движение тела

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    time.sleep(delay)
