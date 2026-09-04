from turtle import *

reset()

#setup
hideturtle()
penup()
width(3)
color("#081C0D")

#Go farther to the left and down
backward(250)
right(90)
forward(100)

#outline
pendown()
begin_fill()
left(45)
forward(200)
left(45)
forward(200)
left(45)
forward(200)
left(45)
forward(325)
left(90)
forward(484)
left(90)
forward(325)
end_fill()
penup()

#lips
color("pink")
left(90)
forward(121)
width(20)
pendown()
forward(242)
penup()

#eyes
left(90)
forward(200)
width(100)
color("white")
pendown()
forward(0.1)
width(75)
color("blue")
forward(0.1)
width(40)
color("black")
forward(0.1)
penup()
left(90)
forward(242)
width(100)
color("white")
pendown()
forward(0.1)
width(75)
color("blue")
forward(0.1)
width(40)
color("black")
forward(0.1)
penup()
penup()


done()
