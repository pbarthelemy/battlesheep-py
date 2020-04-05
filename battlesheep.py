

import array
from enum import Enum



class directions(Enum):
    EAST = [1,0]
    SOUTH = [1,-1]

class sheep(Enum):
    NONE = 0
    WHITE = 1
    BLACK = 2

class stack:
    def __init__(self, player = sheep.NONE, size = 0, hex = None):
        self.player = player
        self.size = size
        self.hexagon = hex
 
class hexagon:
    NONEXISTENT = -1
    EMPTY = 0

    def __init__(self,content = hexagon.NONEXISTENT):
        self.content = content

    def put_stack(self, stack):
        self.content = stack
    
    def check_content(self):
        return self.content



class board:
    MAX_BOARD_DIMENSION = 20
    ABSCISSA = 0
    ORDINATE = 1

    def __init__(self):
        self.board = [[hexagon() for i in range(MAX_BOARD_DIMENSION)] for j in range(MAX_BOARD_DIMENSION)]]

    get_available_neighbours( x, y):
        available_neighbours = None

        for vector in directions: 
            neighbour_coordinates = [x+y for x,y in zip([x,y],vector)]
            if neighbour_coordinates[ABSCISSA] < 0  or neighbour_coordinates[ORDINATE] < 0:
                continue
            hexagon = self.board[neighbour_coordinates[ABSCISSA], neighbour_coordinates[ORDINATE]]
            if hexagon.get




print(__file__)
print(board)

