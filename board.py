import turtle as t
import random
class Board():
    def __init__(self):
        self.tiles = [
            [0, 0, 0, 2],
            [0, 0, 0, 2],
            [0, 0, 2, 2],
            [0, 0, 0, 0]  # Use 0 to represent the empty cell
        ]

    def draw_grid(self):
        grid = t.Turtle()
        grid.penup()
        grid.hideturtle()
        grid.speed(0)

        x, y = -125, 135
        
        for row in self.tiles:
            for tile in row:
                grid.goto(x, y)
                grid.pendown()
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.forward(50)
                grid.right(90)
                grid.penup()
                x += 50
            x = -125
            y -= 50

    def draw_tiles(self):
        t.clear()
        t.penup()
        t.hideturtle()
        t.goto(-100,100)
        t.penup()
        for row in self.tiles:
            for tile in row:
                t.write(tile, align="center", font=("Arial", 14, "normal"))
                t.forward(50)
            t.backward(200)
            t.right(90)
            t.forward(50)
            t.left(90) 