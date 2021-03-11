#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Exercise: Booking Cinema Tickets and Refreshments

You are going to the cinema and want to know the cost.

Create 3 functions.

tickets.  returns the costs of tickets (i.e one or more) purchased.
          Normal tickets cost 10.99.  Wednesdays reduce the cost by 2.00.
          Premium seating adds an extra 1.50 regardless of the day

refreshments. returns the cost of refreshments.  A user could buy 'popcorn' for 2.00 or 'fizzy pop' for 3.50
             
cinema_trip. Adds the cost of tickets and refreshments together.

"""


def tickets(number, day, premium_seating):
    """
    The cost of the cinema ticket.
    Normal ticket cost is $10.99
    Wednesdays reduce the cost by $2.00
    Premium seating adds an extra $1.50 regardless of the day
    
    Parameters:
    ----------
    number: int
        integer value representing the number of seats to book
        
    day: int
        day of the week to book (1 = Monday ... 7 = Sunday)
        
    premium_seating: bool
        boolean True/False.  Are premium seats required.
        
    Returns:
    -------
    float
    """
    #fill in your code here.  
    return 0.0
    

def refreshment(choice ='popcorn'):
    """ 
    The cost of refrehments.  Choices are popcorn or fizzy pop 
    
    Parameters:
    ----------
    choice The users choice of refreshment (default = 'popcorn')
    
    Returns:
    -------
    float
    """

    #fill in your code here
    return 0.0


def cinema_trip(persons, day, premium_seating, treat):
    """ 
    The total cost of going to the cinema 
    
    Parameters:
    ----------
    persons: int
        number of people who need a ticket
        
    day: int
        day of the week to book (1 = Monday, 7 = Sunday)
        
    preimum_seating: bool
            boolean True/False if premium seats are required
            
    treat: str
        string value representing a choice of refreshment 
        
    Returns:
    -------
    float
    """
    #fill in your code here
    return tickets(persons, day, premium_seating) + refreshment(treat)


if __name__ == '__main__':
    persons = 2
    day = 1
    premium_seating = True
    treat = "popcorn"

    total_cost = cinema_trip(persons, day, premium_seating, treat)

    msg = f'today a trip to the cineman will cost you £{total_cost:.2f}'
    print(msg)
    #expected answer = £26.98

    persons = 3
    day = 3
    premium_seating = True
    treat = "fizzy pop"

    total_cost = cinema_trip(persons, day, premium_seating, treat)

    msg = f'today a trip to the cineman will cost you £{total_cost:.2f}'
    print(msg)
    #expected answer = £34.97
