#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: kai
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

clear()
up()
home()
Turtle()

# ok so I am giving bezos a propeller hat
#littel baby child man
color("red")
width(1)
goto(-100,140)
left(25)
down()
begin_fill()
forward(150)
left(100)
circle(77,160)
end_fill()
up()
#lines ---------------------------------
color("black")
goto(-60,227)
right(20)
down()
forward(72)
up()
goto(-55,227)
left(60)
down()
forward(71)
up()
right(40)
#helicopter -----------------------------
color("yellow")
width(1)
goto(-60,235)
dot(20)
right(90)
begin_fill()
down()
forward(55)
circle(10,200)
forward(55)
end_fill()
forward(5)
right(20)
begin_fill()
forward(55)
circle(10,200)
forward(55)
end_fill()
up()
# STICK BUUUUUUUUUUUUUUUUUUUUUUUUUUUG
color(247, 242, 181)
width(4)
left(120)
goto(25,-25)
down()
dot(10)
forward(40)
left(25)
forward(40)
up()
goto(30,-30)
left(190)
down()
forward(40)
left(70)
forward(47)
up()
goto(32,-32)
left(20)
down()
forward(38)
up()
goto(50,-38)
right(70)
down()
forward(30)
left(85)
forward(18)
up()
goto(55,-40)
right(50)
down()
forward(15)
left(20)
forward(17)
up()
goto(55,-40)
left(35)
down()
forward(15)
right(30)
forward(18)
up()
goto(70,-42)
left(50)
down()
forward(35)
right(35)
forward(13)
up()
goto(25,-25)
right(130)
down()
forward(10)
up()
goto(27,-23)
right(20)
down()
forward(10)
up()
# text time text time ------------------
goto(-330,-330)
color("black")
write("get stick bugged lol", font=("Comic Sans MS",50, "normal"))


# VOILA -----------------------------

home()
color("black")





