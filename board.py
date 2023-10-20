import turtle as t
import random
class Board():
    def __init__(self):
        self.tiles = [
            [0, 2, 0, 2],
            [2, 2, 0, 2],
            [2, 0, 2, 2],
            [0, 0, 0, 0]  
        ]
        


    def move_up(self):
        for j in range(4):
            for i in range(1, 4):
                if self.tiles[i][j] != 0:
                    x = i
                    while x > 0 and self.tiles[x-1][j] == 0:
                        self.tiles[x-1][j] = self.tiles[x][j]
                        self.tiles[x][j] = 0
                        x -= 1
                    if x > 0 and self.tiles[x-1][j] == self.tiles[x][j]:
                        self.tiles[x-1][j] += self.tiles[x][j]
                        self.tiles[x][j] = 0
        self.draw_tiles()

    def move_down(self):
        for row in range(4):
            for col in range(2, -1,-1):
                if self.tiles[col][row] != 0:
                    x = col
                    while x > -1 and x < 3 and self.tiles[x+1][row] == 0:
                        self.tiles[x+1][row] = self.tiles[x][row]
                        self.tiles[x][row] = 0
                        x -= 1
                    if x > -1 and x < 3 and self.tiles[x+1][row] == self.tiles[x][row]:
                        self.tiles[x+1][row] += self.tiles[x][row]
                        self.tiles[x][row] = 0
        self.draw_tiles()

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