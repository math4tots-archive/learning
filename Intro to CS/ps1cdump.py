#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:13:41 2018

@author: toto4tots
"""
annual_salary = float((input("annual salary?\n")))
semi_annual_raise = 0.07
low = 0
high = 1000
portion_saved = (high + low)/2.0
down = 1000000*0.25
current_savings = 0
month = 0
while abs(portion_saved*(1/10000)*current_savings - down) > 100:
    if portion_saved*(1/10000) < down:
        low = portion_saved
    if portion_saved*(1/10000) > down:
        high = portion_saved
       
print(portion_saved*(1/10000))

#This won't work because this is not the bisection way 

for r in range(10000):
    if month%6 == 0 and month != 0:
        month += 1
        annual_salary += semi_annual_raise*annual_salary
        interest = (current_savings*0.04)/12
        current_savings += ((annual_salary*portion_saved)/12 + interest)
    else:
        month += 1
        interest = (current_savings*0.04)/12
        current_savings += ((annual_salary*portion_saved)/12 + interest)
#The above gives me the rate itself.
#Below should be t
    if abs(portion_saved*(1/10000)*current_savings - down) > 100:
        if portion_saved*(1/10000) < down:
            low = portion_saved
        if portion_saved*(1/10000) > down:
            high = portion_saved
    else:
        break
    