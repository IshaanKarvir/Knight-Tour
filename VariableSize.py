#!/usr/bin/env python
# coding: utf-8


import chess
import chess.svg
#import cairo
from cairosvg import svg2png
import os

"""
Author: Ishaan Karvir
improvements to simplify dfs - sorts edges in ascending order of how many edges each edge has.  
Generates a series of png images and converts them into a slideshow. 
"""

import time
import sys

class Board:
    '''
    Don't really need a class for board but whatev
    '''

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
            #change x value
            y_value = place[0] + y[i]
            X_value = place[1] + x[i]
            #if X_value == 0 and y_value == 1:
            #    print('edge considered is - ', X_value, y_value, place)
            if not (y_value < 0 or X_value < 0 or y_value > board.size - 1 or X_value > board.size - 1 or board.board[y_value][X_value] == 1):    
                edges.append((y_value, X_value))
        return edges 

def dfs_path_finder(place, Board, path = [], i=0):
    path.append(place)
    Board.board[place[0]][place[1]] = 1
    edges = get_edges(place, Board)
    #reverse is by default false
    edges = sorted(edges, key = Board.func) #this is the key to faster results - makes run times go from 30 seconds to less than a second - comment it out to see
    if len(path) == Board.size ** 2:
        return path
    if len(edges) == 0 and not Board.check():
        Board.board[place[0]][place[1]] = 0
        return False
    for edge in edges:
        result = dfs_path_finder(edge, Board, path, i + 1)
        if result:
            return result
        path.pop()

    #if it goes through all edges without good things happening
    Board.board[place[0]][place[1]] = 0
    # :(
    return False

#Just a lazy function to print the board. Formatted for spacing
def print_board(path, board):
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

def board_string(x, y):
    main_string = "8/8/8/8/8/8/8/8 w"
    if x == 0:
        a = 'N7'
    elif x == 7:
        a = '7N'
    else:
        a = str(x) + 'N' + str(7 - x)
    y_place = 2 * (7 - y)
    main_string = main_string[:y_place] + a + main_string[y_place + 1:]
    return main_string


def main(x, y, z):
    place = (x, y)    
    BOARD = Board(z)
    start = time.time()
    path = dfs_path_finder(place, BOARD)
    print(path )
    end = time.time()
    print_board(path, BOARD)
    print(end - start)
        
main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
# coding: utf-8
