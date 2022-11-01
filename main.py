import turtle
import colorgram
from turtle import Turtle
import random

colors = colorgram.extract("C:\\Users\\michael.waggoner\\PycharmProject\\HirstPainting\\Hirst.jpg",8)
color_list = []
for color in colors:
    tuple = (color.rgb.r,color.rgb.g,color.rgb.b)
    color_list.append(tuple)

screen = turtle.Screen()


tim = Turtle()
screen.colormode(255)

def paint(size,rows):
    tim.penup()
    tim.setx(-size)
    tim.sety(-size)
    tim.seth(0)
    tim.penup()
    for i in range(0,rows + 1):
        while tim.xcor() <= size:
            tim.forward(20)
            random_color = color_list[random.randint(0, 7)]
            tim.dot(5,random_color)
        tim.setx(-size)
        tim.sety(-size + i * 20)

paint(200,30)



screen.exitonclick()























screen = turtle.Screen()
screen.exitonclick()