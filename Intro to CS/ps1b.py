#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:06:14 2018

@author: toto4tots
"""

annual_salary = float((input("annual salary?\n")))
portion_saved = float(input("Portion saved in decimals\n"))
total_cost = float(input("Dream home cost\n"))
semi_annual_raise = float(input("Semi annual raise as decimal\n"))
month = 0
current_savings = 0
while current_savings <= total_cost*0.25:
    if month%6 == 0 and month != 0:
        month += 1
        annual_salary += semi_annual_raise*annual_salary
        interest = (current_savings*0.04)/12
        current_savings += ((annual_salary*portion_saved)/12 + interest)
    else:
        month += 1
        interest = (current_savings*0.04)/12
        current_savings += ((annual_salary*portion_saved)/12 + interest)
   
print(month)
    