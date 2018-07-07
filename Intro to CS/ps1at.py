#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:17:10 2018

@author: toto4tots
"""
print("annual salary?")
annual_salary = float(int(input()))
print("Portion saved in decimals")
portion_saved = float(input())
print("Dream home cost")
total_cost = float(int(input()))

month = 0
current_savings = 0
while current_savings != total_cost*0.25:
    r = current_savings*0.04
    current_savings = ((annual_salary*portion_saved)/12 + r/12)
    month += 1
   
print(month)
    
