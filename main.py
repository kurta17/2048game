import turtle as t
from board import Board
screen = t.Screen()
screen.setup(600,600)
screen.tracer(0)

board = Board()
board.draw_grid()
board.draw_tiles()

screen.listen()
screen.onkey(fun=board.move_up , key="Up")
screen.onkey(fun=board.move_down , key="Down")
screen.onkey(fun=board.move_left , key="Left")
screen.onkey(fun=board.move_right , key="Right")

screen.update()

t.done()