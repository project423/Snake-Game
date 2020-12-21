from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_one(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'Game Over - Score: {self.score}', align=ALIGNMENT, font=FONT)