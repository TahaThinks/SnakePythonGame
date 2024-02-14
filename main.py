import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Taha SnakeGame")

snake = Turtle("square")
snake.color("white")
snake.shapesize(1,3,1)




screen.exitonclick()