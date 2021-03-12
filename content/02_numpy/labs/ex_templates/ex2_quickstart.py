# -*- coding: utf-8 -*-
"""
MATH6005 - Lab 4, exercise 2
Solution.

@author: Carlos Lamas-Fernandez
"""
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    ''' Defines the main parameters and runs the algorithm
    '''

    directory = '../data/pieces'
    piece_names = ['p1.csv', 'p2.csv', 'p3.csv', 'p4.csv', 'p5.csv',
                   'p6.csv', 'p7.csv', 'p8.csv', 'p9.csv', 'p10.csv']

    container_width = 6
    container_height = 12

    piece_list = read_pieces(directory, piece_names)

    container, packed_pieces = top_left_corner(piece_list,
                                               container_width,
                                               container_height)
    # Show final packing
    plot_container(container)

    # See if it was possible to pack all pieces:
    if packed_pieces < len(piece_list):
        print('WARNING: only {0} pieces were packed, out of {1}'.
              format(packed_pieces, len(piece_list)))


def top_left_corner(piece_list, container_width, container_height):
    ''' Top left corner algorithm

    Keyword arguments:
    piece_list -- list of pieces (float numpy arrays)
    container_width -- size of the container along the x axis (int)
    container_height -- size of the container along the y axis (int)
    '''

    packed_pieces = 0
    container = np.zeros((container_height, container_width))

    for piece in piece_list:

        
        # Remove if statement!!!
        if (packed_pieces > 0):
            break
        ###


        piece_placed = False

        for c_row in range(container_height):
            for c_col in range(container_width):
                if not pieces_overlap(container, piece, c_row, c_col):
                    place_piece(container, piece, c_row, c_col)
                    piece_placed = True
                    break
                else:
                    continue

            if piece_placed:
                break

        if piece_placed:
            packed_pieces += 1

    return(container, packed_pieces)


def pieces_overlap(container, piece, x_coord, y_coord):
    '''Returns true if the piece overlaps with others, false if not

    Keyword arguments:
    container -- binary representation of the container (numpy array)
    piece -- binary representation of the piece tested (numpy array)
    x_coord -- x position in the container (int)
    y_coord -- y position in the container (int)
    '''

    # Check for overlap, if found, return True

    return False


def place_piece(container, piece, x_coord, y_coord):
    ''' Modifies the container to have piece placed at position (x,y)

    Keyword arguments:
    container -- binary representation of the container (numpy array)
    piece -- binary representation of the piece placed (numpy array)
    x_coord -- x position in the container (int)
    y_coord -- y position in the container (int)
    '''

    p_x, p_y = piece.shape

    container_bit = container[x_coord:x_coord + p_x, y_coord:y_coord + p_y]
    container_bit += piece


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
    n_pieces = len(piece_names)
    piece_list = []
    for pname in piece_names:
        piece = np.loadtxt(directory + os.sep + pname,
                           delimiter=',',
                           dtype=np.float64,
                           ndmin=2)

        # Add a small random number to have different colours in the plot
        piece = piece*(1 + 0.1 + (1 + len(piece_list))/n_pieces*0.4)
        piece_list.append(piece)

    return piece_list


def plot_container(container):
    ''' Plots the contents of the container

    To have different colours, loops through the pieces and changes their
    value from 1.xx to their index + 2

    Keyword arguments:
    container -- binary representation of the container (numpy array)
    '''

    container_for_plot = container

    n_pieces = 0
    while True:
        min_val = np.min(container_for_plot[container_for_plot > 0])
        if min_val > 2:
            break

        container_for_plot[container_for_plot == min_val] = n_pieces + 2

        n_pieces += 1

    plt.imshow(container_for_plot, cmap='tab20b')

if __name__ == "__main__":
    main()
