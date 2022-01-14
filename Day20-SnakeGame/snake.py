from turtle import Turtle

MOVE_DIST = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake:
    
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((i*-20,0))
        self.head = self.segments[0]
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].setposition(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def heading_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
    
    def heading_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def heading_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def heading_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())