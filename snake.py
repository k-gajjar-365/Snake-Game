from turtle import Turtle,Screen

SEGMENT_CORDS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in SEGMENT_CORDS:
            self.add_segment(i)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snakes.append(new_segment)

    def reset_snake(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]


    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
       for i in range(len(self.snakes)-1,0,-1):
           new_x = self.snakes[i-1].xcor()
           new_y = self.snakes[i-1].ycor()
           self.snakes[i].goto(new_x,new_y)
       self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.snakes[0].heading()== 270 and not self.snakes[0].heading()==90 :
            if self.snakes[0].heading()==180:
                self.snakes[0].right(90)
            else:
                self.snakes[0].left(90)


    def down(self):
        if not self.snakes[0].heading()==90 and not self.snakes[0].heading()==270:
            if self.snakes[0].heading()==180:
                self.snakes[0].left(90)
            else:
                self.snakes[0].right(90)


    def right(self):
        if self.snakes[0].heading()==270:
            self.snakes[0].left(90)
        elif not self.snakes[0].heading()==180:
            self.snakes[0].right(90)
        else:
            self.snakes[0].right(90)


    def left(self):
        if self.snakes[0].heading()==270:
            self.snakes[0].right(90)
        elif not self.snakes[0].heading()==0:
            self.snakes[0].left(90)
        else:
            self.snakes[0].left(90)
