from turtle import *
from random import *
import turtle
import time

# SCREEN SETUP
setup(800, 500)
title("เต่านักวิ่ง")
bgcolor("brown")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("white")
write("TURTLE RUN!", font=("Arial", 20, "bold"))

# DIRT
goto(-350, 200)
pendown()
color("grey")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size=20
shape("square")
penup()

#WHITE SQUARES ROW 
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

for i in range(10):
    goto(250 + gap_size,  ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

#BLACK SQUARES ROW
color("black")
for i in range(10):
        goto(250, (190 - (i * gap_size * 2)))
        stamp()
for i in range(10):
       goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
       stamp()

# TURTLE 1 - CYAN
blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

# TURTLE 2 - PINK
pink_turtle = Turtle()
pink_turtle.color("pink")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300, 50)
pink_turtle.pendown()

# TURTLE 3 - GREEN
green_turtle = Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300, -50)
green_turtle.pendown()

# TURTLE 4 - RED
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5)
red_turtle.penup()
red_turtle.goto(-300, -150)
red_turtle.pendown()

# pause for 1 sec before racing
time.sleep(1)

# MOVE THE BLUE TURTLE
while blue_turtle.xcor() <= 230 and  pink_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and red_turtle.xcor() <=230 : 
    blue_turtle.forward(randint(1, 10))
    pink_turtle.forward(randint(1, 10))
    green_turtle.forward(randint(1, 10))
    red_turtle.forward(randint(1, 10))

# ชัยชนะของผู้ชนะ celebrate

if blue_turtle.xcor() > pink_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > red_turtle.xcor():
    print("Blue turtle wins!")
    for i in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.5)

elif pink_turtle.xcor() > blue_turtle.xcor() and pink_turtle.xcor() > green_turtle.xcor() and pink_turtle.xcor() > red_turtle.xcor():
    print("Pink turtle wins")
    for i in range(72):
       pink_turtle.right(5)
       pink_turtle.shapesize(2.5)

elif green_turtle.xcor() > blue_turtle.xcor() and green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > red_turtle.xcor():
    print("Green turtle wins")
    for i in range(72):
       green_turtle.right(5)
       green_turlte.shapesize(2.5)

elif red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > green_turtle.xcor():
    print("Red turtle wins")
    for i in range(72):
       red_turtle.right(5)
       red_turlte.shapesize(2.5)



    
