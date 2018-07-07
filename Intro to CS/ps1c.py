#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 07:22:48 2018

@author: toto4tots
"""
#r = rate
#down = total_cost*0.25

annual_salary = float((input("annual salary?\n")))
semi_annual_raise = 0.07
month = 0
current_savings = 0
high = 10000
low = 0
saved_rate = (high + low)/2
down = 1000000*0.25
   
while abs(saved_rate*(1/10000)*current_savings - down) > 100:
    if saved_rate*(1/10000) < down:
        month += 1
        low = saved_rate
        
    if saved_rate*(1/10000) > down:
            high = saved_rate
    
            
print(saved_rate*(1/10000))
    
    
def calculation(current_savings,  annual_salary, semi_annual_raise):
  




#annual_salary = float((input("annual salary?\n")))
#portion_saved = float(input("Portion saved in decimals\n"))
#total_cost = float(input("Dream home cost\n"))
#semi_annual_raise = float(input("Semi annual raise as decimal\n"))
#month = 0
#current_savings = 0
#while current_savings <= total_cost*0.25:
#    if month%6 == 0 and month != 0:
#        month += 1
#        annual_salary += semi_annual_raise*annual_salary
#        interest = (current_savings*0.04)/12
#        current_savings += ((annual_salary*portion_saved)/12 + interest)
#    else:
#        month += 1
#        interest = (current_savings*0.04)/12
#        current_savings += ((annual_salary*portion_saved)/12 + interest)
#   
#print(month)
