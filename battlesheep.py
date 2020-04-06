

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
        available_neighbours = []

        for vector in directions: 
            distance = 1
            possible_move = [x+y for x,y in zip([x,y],vector)]
            while
            vector = map(lambda x: x * distance, vector)
            possible_move = [x+y for x,y in zip([x,y],vector)]

            hexagon = self.board[neighbour_coordinates[ABSCISSA], neighbour_coordinates[ORDINATE]]
            if hexagon.check_content == hexagon.EMPTY:
                possible_move = neighbour_coordinates
                while hexagon.check_content == hexagon.EMPTY:





print(__file__)
print(board)

