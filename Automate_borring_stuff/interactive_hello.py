#!/usr/bin/python3
'''This program say hello an ask for my name'''

import time

print('Hello There!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName.title())
time.sleep(2)
print('The lenght of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
time.sleep(2)
print('Good bye!')
