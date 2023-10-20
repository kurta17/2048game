import turtle as t
import random
import time 

class Board():
    def __init__(self):
        self.tiles = [
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [2, 0, 2, 0]  
        ]
        self.count_step = 0
        


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
        self.random_num()
        self.count_step += 1

    def move_down(self):
        for row in range(4):
            for col in range(2, -1,-1):
                if self.tiles[col][row] != 0:
                    x = col
                    while x > -1 and x < 3 and self.tiles[x+1][row] == 0:
                        self.tiles[x+1][row] = self.tiles[x][row]
                        self.tiles[x][row] = 0
                        x += 1
                    if x > -1 and x < 3 and self.tiles[x+1][row] == self.tiles[x][row]:
                        self.tiles[x+1][row] += self.tiles[x][row]
                        self.tiles[x][row] = 0
        self.random_num()
        self.count_step += 1

    def move_left(self):
        for col in range(4):
            for row in range(1,4):
                if self.tiles[col][row] != 0:
                    x = row
                    while x > 0 and self.tiles[col][x - 1] == 0:
                        self.tiles[col][x - 1] = self.tiles[col][x]
                        self.tiles[col][x] = 0
                        x -= 1
                    if x > 0 and self.tiles[col][x - 1] == self.tiles[col][x]:
                        self.tiles[col][x - 1] += self.tiles[col][x]
                        self.tiles[col][x] = 0 
                     
        self.random_num()
        self.count_step += 1

    def move_right(self):
        for col in range(4):
            for row in range(2,-1,-1):
                if self.tiles[col][row] != 0:
                    x = row
                    while x < 3  and self.tiles[col][x + 1] == 0:
                        self.tiles[col][x + 1] = self.tiles[col][x]
                        self.tiles[col][x] = 0
                        x += 1
                    if x < 3 and self.tiles[col][x + 1] == self.tiles[col][x]:
                        self.tiles[col][x + 1] += self.tiles[col][x]
                        self.tiles[col][x] = 0 
                     
        self.random_num()
        self.count_step += 1

    def empty_cell(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j] == 0:
                    empty.append((i,j))
        return empty

    def random_num(self):
        empty = self.empty_cell()
        x = random.randint(0,len(empty) - 1)
        row = empty[x][0]
        col = empty[x][-1]
        if self.count_step % 2 == 0:
            self.tiles[row][col] = 2
        self.draw_tiles()

    def you_won(self):
        for j in range(4):
            for i in range(1, 4):
                if self.tiles[i][j] == 2048:
                    return True
        return False      

    def print_won(self):
        win = t.Turtle()
        win.hideturtle()
        win.penup()
        win.goto(0,240)
        win.write("You Won!", align="center", font=("Arial", 40, "normal"))        
        
    def no_valid_moves(self):
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j] == 0:
                    return False 
                if i > 0 and self.tiles[i][j] == self.tiles[i - 1][j]:
                    return False
                if i < 3 and self.tiles[i][j] == self.tiles[i + 1][j]:
                    return False
                if j > 0 and self.tiles[i][j] == self.tiles[i][j - 1]:
                    return False
                if j < 3 and self.tiles[i][j] == self.tiles[i][j + 1]:
                    return False
        return True  

    def print_gameover(self):
        win = t.Turtle()
        win.hideturtle()
        win.penup()
        win.goto(0,240)
        win.write("Game Over!", align="center", font=("Arial", 40, "normal"))    

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