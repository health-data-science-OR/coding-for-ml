#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Debug Exercise Python Lab 1

The code below has a number of bugs.  

Can you fix the code and help it to run?


"""

def split_word_in_two(to_split):
"""
Returns string split into two parts

If the word's length is even the two parts have
equal number of characters

Keyword arguments:
to_split -- the string to split int o
"""
length = len(to_spit)
half_length = length / 2

part1 = to_split[:half]
part2 = to_split[half:]

return part1, part2


def main():
"""
Tests the split_word_in_two function.
Input word = 'faster'
Expected output = ('fas', 'ter')
"""
word_to_split = 'faster'
result = split_word_in_two(word_to_split)
print('Part 1 = {0}; Part 2 = {1}'.format(result[0], result[1]))


if __name__ == "__main__":
   main()

