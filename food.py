from turtle import Turtle

from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.new_food()

    def new_food(self):
        self.goto(randint(-280,280), randint(-280,280))


    

