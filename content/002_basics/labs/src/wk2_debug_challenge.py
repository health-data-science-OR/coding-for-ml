#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Week 2: Debug Challenge.

This weeks debug challenges loops and nested loops.

A classic task in programming is to sort a list.  Python makes this 
very simple by including a number of ways to sort a list.  

Under the hood the sorting routines are all variations on loops 
where values in the array are swapped until it is in ascending order.

The function below implements insertion sort.  Insertion sort is an 
efficient algorithm for sorting a list made of two loops.  An outer loop
that iterates forward through the list and an inner list that iterates backwards.

The code below is not running.  Can you debug it?

Good luck!


"""

def insertion_sort(to_sort):
    """
    Sort a list of numbers using the insertion sort algorithm
    Return a list of sorted numbers
    
    Keyword arguments:
    to_sort -- an unsorted python list of numbers
    """
    
    #This is the outer loop.
    for i in range(1, to_sort):
        
        j = i
        
        #This inner while loop.  Note the backwards iteration.
        #The while loop terminates when either:
        #1. j == 0 i.e. the first element in the list is reached
        #2. there is no need to do any sorting i.e. to_sort[j-1] < to_sort[j]
        while j > 0 and to_sort[j-1] > to_sort[j]
            
         #to swap the values we need a 3rd variables (temp)
         temp = to_sort[j]
         to_sort[j] = to_sort[j-1]
         to_sort[j-1] = temp
         j -= 1
        
    return to_sort


if __name__ == "__main__":
   list_to_sort = [14,33,27,10,35,19,42,44]
   sorted_list = insertion_sort(list_to_sort)
   print(sorted_list)