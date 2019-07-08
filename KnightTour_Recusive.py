"""

Ishaan Karvir
improvements to simply dfs - sorts edges in ascending order of how many edges each edge has. 
 
"""
import time
import sys

class Board:

    #sorting parameter
    def func(self, x):
        return len(get_edges(x, self))
    
    def __init__(self, size):
        self.board = [[0 for i in range (size)] for a in range(size)]
        self.size = size
    
    def check(self):
        for row in self.board:
            for index in row:
                if index == 0:
                    return False
        return True
    
    def __repr__(self):
        return str(self.board)
    
    def reset(self):
        self.board = [[0 for i in range (self.size)] for a in range(self.size)]


def get_edges(place, board):
        x = [2, 1, -1, -2, -2, -1, 1, 2]
        y = [1, 2,  2,  1 ,-1, -2, -2, -1 ]
        edges = []
        for i in range(len(x)):
            y_value = place[0] + y[i]
            X_value = place[1] + x[i]
            if not (y_value < 0 or X_value < 0 or y_value > board.size - 1 or X_value > board.size - 1 or board.board[y_value][X_value] == 1):    
                edges.append((y_value, X_value))
        return edges 

def dfs_path_finder(place, Board, path = []):
    path.append(place)
    Board.board[place[0]][place[1]] = 1
    edges = get_edges(place, Board)
    edges = sorted(edges, key = Board.func)
    if len(path) == Board.size ** 2:
        return path
    if len(edges) == 0 and not Board.check():
        Board.board[place[0]][place[1]] = 0
        return False
    for edge in edges:
        result = dfs_path_finder(edge, Board, path)
        if result:
            return result
        path.pop()
    Board.board[place[0]][place[1]] = 0
    return False

def print_board(path, board):
    #displays the board - pretty inefficient but does the job
    space = str(len(str(board.size ** 2)))
    for i in range(board.size):
        for j in range(board.size):
            counter = 1
            for a in path:
                if a == (i, j):
                    print( ("%"+ space +".0f") % counter, end = '  ' )
                    break
                counter += 1
        print('\n')    

def verify(path):
    for item in path:
        if path.count(item) > 1:
            return False
    return True


def main():
    #sys.setrecursionlimit(2000)
    # Will need to change recusion limit for board sizes over 30 
    place = (0, 0)    
    if len(sys.argv) ==  1:
        BOARD = Board(8)
    else:
        BOARD = Board(int(sys.argv[1]))

    start = time.time()
    path = dfs_path_finder(place, BOARD)
    end = time.time()
    print_board(path, BOARD)
    print(end - start)
    print(verify(path))

if __name__ == '__main__':
    main() 
