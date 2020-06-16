#!/usr/bin/env python3
"""Python script to Check if a string is a
palindrome or could be one by
changing only one character"""


def IsCasiPalindormo(str):
    """Function to check if it is possible to
    convert the string into palindrome"""
    n = len(str)
    count = 0
    for i in range(0, int(n / 2)):
        if (str[i] != str[n - i - 1]):
            count += 1
    if count == 0:
        return True  # 'es palindromo'
    elif count == 1:
        return True  # 'modificando una letra es palindromo'
    return False  # 'no es palindromo modificando solo una letra'


# Examples

string = 'abccba'
IsCasiPalindormo(string)

string = 'abccbx'
IsCasiPalindormo(string)

string = 'abccfx'
IsCasiPalindormo(string)
