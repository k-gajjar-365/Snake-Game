from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Courier",20,"bold")


def get_score():
    with open("data.txt", mode="r") as file:
        return int(file.read())

def write_score(highest_score):
    with open("data.txt","w") as file:
        file.write(str(highest_score))

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
        self.clear()
        self.write(arg=f"Score : {self.score} | Highest score : {get_score()}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > get_score():
            write_score(self.score)
        self.score = 0
        self.update_screen()

    def scoring(self):
        self.score+=1
        self.update_screen()

