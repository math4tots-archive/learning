#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:53:31 2018

@author: toto4tots
"""

n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? \n")
c = 0
while n == "right" or n == "Right":
    c += 1
    if c < 3:
        print("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? \n")
        n = input()
    else:
        print("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
        n = input()
print("\nYou got out of the Lost Forest!\n\o/")

        






#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
##s = input("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? ")
#c = 0
#while n == "right"or n == "Right":
#    c += 1
#    if c < 3:
#        print(c)
#        print(n)
#    else:
#        print(c)
#        print(n)
#        if input() != "right" or input() != "Right":
#            break
#print("\nYou got out of the Lost Forest!\n\o/")
#        
#        
##        print(n)
##    if c == 2:
##        print(input("You are in the Lost Forest\n****************\n****************\n :(\n****************\n****************\nGo left or right? "))
##    else:
##        print(input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? "))
##print("\nYou got out of the Lost Forest!\n\o/")
##        
##        
