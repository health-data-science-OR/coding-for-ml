#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Week 1 Extra Material: If-then statements
    
A short look ahead at conditionals and if statements.

We will cover these in detail in week 2.  But feel free to have edit the code
below to see how it works.

In most Python programmes that you write you will be using if-then statements.  
These allow you to make conditional choices in your code.  

To use if-then statements you need to understand

a.) boolean comparisons e.g. x > 1
b.) if, elif and else statements
c.) Python whitespace and indentation rules

@author: tom
"""

#%%

# =============================================================================
# Boolean comparisons - return True or False
# =============================================================================

foo = 2
bar = 'spam'

print('is foo equal to 2?: {0}'.format(foo == 2)) 
print('is foo less than or equal to 5?: {0}'.format(foo <= 5)) 
print('is foo greater than or 100?: {0}'.format(foo > 5)) 

print("is bar equal to 'eggs': {0}".format(bar == 'eggs')) 
print("is bar the same type as foo?: {0}".format(type(bar) == type(foo)))

#%%

# =============================================================================
# We use boolean comparisons in 'if' statements
# =============================================================================

foo = 100  # why not try changing the value of foo to 10, 'bar' and 'eric'

if foo == 100:
    #notice that the print statement is indented.  
    #This is mandatory in python.  Otherise you get an error!
    print("Hello! You branched here, because foo == 100 evaluated to 'True'")
elif foo == 10:
    print("Hello again, you branched here because foo equals 10 this time")
elif foo == 'bar':
    print("Gosh, hello. This time foo looked a bit different!")
else:
    print("So foo didn't equal any of the above. I am the default branch")

#%%

