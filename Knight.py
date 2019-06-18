"""
Knight class
Attributes:
    place: current place on board (idk yet)
    edges: possible places knight could jump to
"""
class Knight:
    def __init__(self, place):
        self.place = place

    def dfs_path_finder(self, place, Board, path = []):
        path.append(place)
        #if place == (1, 4):
        #    print("1, 4 being considered", path)
        Board.board[place[0]][place[1]] = 1
        edges = get_edges(place, BOARD)
        #print(path, len(edges), 'edges found\n')
        #print(edges)
        if len(path) == 64:
            print('found')
            return path
        if len(edges) == 0 and not Board.check():
            #print(place, "put back")
            #if place == (0, 1):
                #print("GOT UNSELECTED", path)
            Board.board[place[0]][place[1]] = 0
            return False
        for edge in edges:
            #print('trying', edge, len(path))
            #if edge in path:
                #print('Somethings really wrong', edge, edges, place)
            #print(edge)
            #if place == (1, 4) and edge == (0, 1):
            #    print('found')
            result = self.dfs_path_finder(edge, Board, path)
            if result:
                return result
            path.pop()
        #if place == (0, 1):
        #    print("Got unselected ")
        Board.board[place[0]][place[1]] = 0
        #print('I have tried every one of ', place, ' edges' )
        #if path == [(2, 2), (1, 4), ]
        return False



class Board:
    def __init__(self):
        self.board = [[0 for i in range (8)] for a in range(8)]
    def check(self):
        for row in self.board:
            for index in row:
                if index == 0:
                    return False
        return True
    def __repr__(self):
        return str(self.board)
    def reset(self):
        self.board = [[0 for i in range (8)] for a in range(8)]

def get_edges(place, board):
        x = [2, 1, -1, -2, -2, -1, 1, 2]
        y = [1, 2,  2,  1 ,-1, -2, -2, -1 ]
        edges = []
        for i in range(len(x)):
            #change x value
            y_value = place[0] + y[i]
            X_value = place[1] + x[i]
            #if X_value == 0 and y_value == 1:
            #    print('edge considered is - ', X_value, y_value, place)
            if y_value < 0 or X_value < 0 or y_value > 7 or X_value > 7:
                #if X_value == 0 and y_value == 1:
                #    print('this is why not selected - out of bounds', X_value, y_value)
                continue
            if board.board[y_value][X_value] == 1:
                #if X_value == 0 and y_value == 1:
                #    print('this is why not selected - already selected')
                continue
            #print('This edge was selected - ', X_value, y_value)    
            edges.append((y_value, X_value))
        return edges


def verify(path):
    for item in path:
        if path.count(item) > 1:
            return False
    return True



BOARD = Board()
KNIGHT = Knight((0, 0))
path = KNIGHT.dfs_path_finder((0, 1), BOARD)
print(path)
BOARD.reset
path = Knight.dfs_path_finder((0, 2), BOARD)
print(path)

"""
for i in range(8):
    for j in range(8):
        BOARD.reset
        print("Trying", i, j)
        path = KNIGHT.dfs_path_finder((i, j), BOARD)p
        if path:
            print(path)
"""
