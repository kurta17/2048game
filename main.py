import turtle as t
from board import Board
screen = t.Screen()
screen.setup(600,600)
screen.tracer(0)

board = Board()
board.draw_grid()
board.draw_tiles()


t.done()