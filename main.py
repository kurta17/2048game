import turtle as t
from board import Board
import time

screen = t.Screen()
screen.setup(600, 600)
screen.tracer(0)

board = Board()

board.draw_grid()
board.draw_tiles()

screen.listen()
screen.onkey(fun=board.move_up, key="Up")
screen.onkey(fun=board.move_down, key="Down")
screen.onkey(fun=board.move_left, key="Left")
screen.onkey(fun=board.move_right, key="Right")

game_over = False

def close():
    t.bye()
    

while not game_over:
    screen.update()
    if board.you_won():
        board.print_won()
        t.update()
        time.sleep(2)
        close()
    if board.no_valid_moves():
        game_over = True
        board.print_gameover()
        t.update()
        time.sleep(2)
        close()
        
t.done()