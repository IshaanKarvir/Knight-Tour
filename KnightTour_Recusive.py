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

        
def dfs_path_finder(place, Board, path = []):
    path.append(place)
    Board.board[place[0]][place[1]] = 1
    edges = get_edges(place, BOARD)
    if len(path) == 64:
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


def get_edges(place, board):
        x = [2, 1, -1, -2, -2, -1, 1, 2]
        y = [1, 2,  2,  1 ,-1, -2, -2, -1 ]
        edges = []
        for i in range(len(x)):
            y_value = place[0] + y[i]
            X_value = place[1] + x[i]
            if not (y_value < 0 or X_value < 0 or y_value > 7 or X_value > 7 or board.board[y_value][X_value] == 1):    
                edges.append((y_value, X_value))
        return edges


def verify(path):
    for item in path:
        if path.count(item) > 1:
            return False
    return True
