from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Courier",25,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,265)
        self.color("white")
        self.hideturtle()
        self.score=0
        self.update_screen()

    def update_screen(self):
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=("Courier",28,"bold"))


    def scoring(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)


