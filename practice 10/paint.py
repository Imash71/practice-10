import turtle
screen = turtle.Screen()
screen.title("Paint App")
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
# tools
tool = "pen"
color = "black"
# movement
def up():
   t.setheading(90)
   t.forward(10)
def down():
   t.setheading(270)
   t.forward(10)
def left():
   t.setheading(180)
   t.forward(10)
def right():
   t.setheading(0)
   t.forward(10)
# tools
def pen_mode():
   global tool
   tool = "pen"
   t.pendown()
   print("Pen mode")
def eraser():
   global tool
   tool = "eraser"
   t.pencolor("white")
   print("Eraser mode")
def color_red():
   t.pencolor("red")
def color_blue():
   t.pencolor("blue")
def color_black():
   t.pencolor("black")
# shapes
def circle():
   t.circle(50)
def rectangle():
   for _ in range(2):
       t.forward(100)
       t.left(90)
       t.forward(50)
       t.left(90)
# keyboard
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(pen_mode, "p")
screen.onkey(eraser, "e")
screen.onkey(color_red, "r")
screen.onkey(color_blue, "b")
screen.onkey(color_black, "k")
screen.onkey(circle, "c")
screen.onkey(rectangle, "x")
t.pendown()
screen.mainloop()