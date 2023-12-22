from turtle import Turtle

""" Shortcut to the code below """
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

""" Creating constants for Snake movement"""
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake_body = []
        self.create_snake()
        self.snake_head = self.full_snake_body[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(0.98)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.full_snake_body.append(new_segment)

    def extend(self):
        self.add_segment(self.full_snake_body[-1].position())

    def snake_move(self):
        for i_num in range(len(self.full_snake_body) - 1, 0, -1):
            """ The x_cor and y_cor is the new coordinate when the snake moves """
            new_x_cor = self.full_snake_body[i_num - 1].xcor()
            new_y_cor = self.full_snake_body[i_num - 1].ycor()
            self.full_snake_body[i_num].goto(new_x_cor, new_y_cor)

        self.full_snake_body[0].forward(MOVE_DISTANCE)

    def move_up(self):
        """ To prevent the snake from turning the opposite direction"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_left(self):
        """ To prevent the snake from turning the opposite direction"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def move_down(self):
        """ To prevent the snake from turning the opposite direction"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        """ To prevent the snake from turning the opposite direction"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
