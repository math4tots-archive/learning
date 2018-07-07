#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:17:10 2018

@author: toto4tots
"""

annual_salary = float((input("annual salary?\n")))
portion_saved = float(input("Portion saved in decimals\n"))
total_cost = float(int(input("Dream home cost\n")))

month = 0
current_savings = 0
while current_savings <= total_cost*0.25:
    month += 1
    interest = (current_savings*0.04)/12
    current_savings += ((annual_salary*portion_saved)/12 + interest)
   
print(month)
    
