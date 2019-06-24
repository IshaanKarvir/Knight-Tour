import time

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
        self.board = [[0 for i in range (7)] for a in range(7)]

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
    return True and (len(path) == 64)


def dfs_path_finder(place, Board):
    path = []
    path.append(place)
    i = 0
    edge_counter = [0 for i in range(64)]
    edge_counter_index = 1
    while (len(path) < 64):
        #gets all the edges
        edges = get_edges(path[len(path) - 1], Board)
        #gets edge number we're looking at
        edge_number = edge_counter[edge_counter_index]
        #increment the edge number of the particular plac
        #moves to the next edge 
        #if runs out of edges
        if edge_number >= len(edges) or (len(edges) == 0 and not Board.check()):
            Board.board[path[-1][0]][path[-1][1]] = 0
            edge_counter[edge_counter_index] = 0    
            path.pop()
            #changes the array number
            edge_counter_index -= 1

        #if the edge works
        else:
            edge = edges[edge_number]
            Board.board[edge[0]][edge[1]] = 1
            path.append(edge)
            #moves to the nex edge
            edge_counter[edge_counter_index] += 1
            #changes the array number 
            edge_counter_index += 1      
    return path

def main():
    BOARD = Board()
    start = time.time()
    path = dfs_path_finder((0, 4), BOARD)
    end = time.time()
    print(path)
    print(end - start)
    print(len(path))
    print(verify(path))

if __name__ == '__main__':
    main()
