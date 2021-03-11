#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:03:41 2019

@author: tom
"""

from py_finance import pv, print_pv

future_value = 1000
rate = 0.05
years = 10
result = pv(future_value, rate, years)

print_pv(future_value, rate, years, result)   
