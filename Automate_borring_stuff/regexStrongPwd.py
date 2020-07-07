#!/usr/bin/env python3
"""
Strong Password Detection with Regexes.
A strong password is defined as one that has:
at least eight characters long, 
at least an uppercase character,
at least a lowercase character,
at least one digit, and
at least one special character.
"""

import re
pwdInsecure = True


def passwordStrength():
    """Function to check if a password is Strong"""
    passwordText = input('Enter Password: ')
    charPattern = re.compile(r'(\w{8,})')
    lowerPattern = re.compile(r'[a-z]+')
    upperPattern = re.compile(r'[A-Z]+')
    digitPattern = re.compile(r'[0-9]+')
    speciPattern = re.compile(r'[^a-z0-9]+')

    charRegex = charPattern.findall(passwordText)
    lowerRegex = lowerPattern.findall(passwordText)
    upperRegex = upperPattern.findall(passwordText)
    digitRegex = digitPattern.findall(passwordText)
    speciRegex = speciPattern.findall(passwordText)
    ''' TODO: Enter conditions to see if password passes all checks and then return
    a message if it does.'''
    if charRegex == []:  # Checks if the password does not contain 8 characters
        print('Password must contain at least 8 characters')
    elif lowerRegex == []:  # Checks if the password does not contain a lowercase character
        print('Password must contain at least one lowercase character')
    elif upperRegex == []:  # Checks if the password does not contain an uppercase character
        print('Password must contain at least one uppercase character')
    elif digitRegex == []:  # Checks if the password does not contain a digit character
        print('Password must contain at least one digit character')
    elif speciRegex == []:  # Checks if the password does not contain a digit character
        print('Password must contain at least one special character')
    else:
        print('Your password is strong. Good job!')
        global pwdInsecure
        # Set global variable to access it outside function.
        pwdInsecure = False
        return

while pwdInsecure:
    passwordStrength()
