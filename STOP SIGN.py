#CS501A
#Ezinne Ndumnwere
#Turtle

import math
import turtle

# Named constants  
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# Initialize turtle 
t = turtle.Turtle()

# Set up window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT) 
turtle.speed(ANIMATION_SPEED)

# Calculate diameter
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Move turtle to start
t.penup()
t.goto(0, -diameter / 2) 

# Draw octagon
t.pendown()
for _ in range(NUM_SIDES):
  t.forward(LENGTH)
  t.left(ANGLE)

# Move turtle to text position  
t.penup()
t.goto(TEXT_X, TEXT_Y)

# Write text
t.color("red")
t.write("STOP", align="center", font=("Rockwell Extra Bold", 24, "normal")) 

# Hide turtle
t.hideturtle()

