#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:55:48 2018

@author: toto4tots
"""
#trying to find the cube root of a number
#Q:why would I use a for loop for this? I don't know when 
#the user will get to the right number?
#ANS: Be smart about this. The cubed number would be less than
#the cube. Also the for loop is for the computer not the user. 

cube = int(input("What cube number would you like to find?\n"))
for guess in range(cube + 1):
    if guess**3 == cube:
        print("I think it's this one!" + " " + str(guess))
    if guess**3 != cube:
        print("I don't think this is a perfect cube!")
        break

#Professor's code:
    #for guess in range(abs(cube)+1):
#    # passed all potential cube roots
#    if guess**3 >= abs(cube):
#        # no need to keep searching
#        break
#if guess**3 != abs(cube):
#    print(cube, 'is not a perfect cube')
#else:
#    if cube < 0:
#        guess = -guess
#    print('Cube root of ' + str(cube) + ' is ' + str(guess))
