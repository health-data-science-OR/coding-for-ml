#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is used to demonstrate how to avoid code running on
import.

It contains some example functions.

Example usage:

import py_finance
"""

def pv(future_value, rate, n):

   '''
   Discount a value at defined rate n time periods into the future.

   Forumula:
   PV = FV / (1 + r)^n
   Where
   FV = future value
   r = the comparator (interest) rate
   n = number of years in the future

   Keyword arguments:
   future value -- the value to discount
   rate -- the rate at which to do the discounting
   n -- the number of time periods into the future
   '''
   return future_value / (1 + rate)**n


def print_pv(future_value, rate, n, present_value):
   '''
   Prints a sentence reporting the present value of a
   future_value assuming a rate in n time units

   Keyword arguments:
   future value -- the value to discount
   rate -- the rate at which to do the discounting
   n -- the number of time periods into the future
   present_value -- the present value of the transaction
   '''
   msg = 'Using an interest rate of {0}, ' + \
      'a payment of £{1:.2f} in {2} years time is worth £{3:.2f} today'

   print(msg.format(rate, future_value, n, present_value))


def test_case1():
   #Test case 1
   future_value = 2000
   rate = 0.035
   years = 5
   result = pv(future_value, rate, years)

   print_pv(future_value, rate, years, result)

def test_case2():
   #Test case 2
   future_value = 350
   rate = 0.01
   years = 10
   result = pv(future_value, rate, years)

   print_pv(future_value, rate, years, result)

def main():
   test_case1()
   test_case2()



if __name__ == '__main__':
   main()




