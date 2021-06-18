# -*- coding: utf-8 -*-
"""
Lab 4 - Debug Challenge

@author: Carlos Lamas-Fernandez
"""
import numpy as np
import matplotlib.pyplot as plt

def main():
    ''' Defines the main parameters and runs the algorithm
    '''

    directory = '../data/pieces'
    piece_names = ['p1.csv', 'p2.csv', 'p3.csv', 'p4.csv', 'p5.csv',
                   'p6.csv', 'p7.csv', 'p8.csv', 'p9.csv', 'p10.csv']

    piece_list = read_pieces(directory, piece_names)
    
    
    # Print information for the pieces:
    for p_i in piece_list:
        # Print the piece first:
        print('===== PIECE {0}=====')
        print_piece(p_i)
        
    print('Piece rotations:')
    for rot in range(4):
        print('Rotated {0} degrees:'.format(90*rot)
    p_i = rotate_right(p_i)
    print_piece(p_i)


def rotate_right(piece)
    ''' Rotate a piece to the right.
    We first transpose it and then flip it horizontally
    '''
    rotated_piece = np.transpose(piece)
    rotated_piece = np.fliplr(piece)
    return(rotated_piece)

def print_piece(piece):
    ''' Shows the piece on screen
    '''
    plt.imshow(-1*piece, cmap='gray')
    plt.show()    
        
        

def read_pieces(directory, piece_names):
    ''' Returns a list of pieces composed of numpy arrays for each of them

    The pieces should be in the directory "directory" and their names listed
    in the list "piece_names". It is expected that pieces are CSV files
    containing only 0 and 1 values. The function adds a small random number
    (i.e. <= 0.4) in order to achieve different colours when plotting the
    resulting container.

    Keyword arguments:
    directory -- string containing the name of directory of the piece files
    piece_names -- list with the names of the piece CSV files
    x -- x position in the container (int)
    y -- y position in the container (int)
    '''
    piece_list = []
    for pname in piece_names:
        piece = np.loadtxt(directory + os.sep + pname,
                           delimiter=',',
                           dtype=np.float64,
                           ndmin=2)

        piece_list.append(piece)

    return piece_list

if __name__ == "__main__":
    main()
