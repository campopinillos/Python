#!/usr/bin/python3
''' Interactive while loop'''
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')
