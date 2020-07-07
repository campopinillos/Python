#!/usr/bin/env python3

""""Justifying Text with rjust(), ljust(), and center()"""
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('\n' + 'PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

spam = 'Hello'
print(spam.rjust(30))
print(spam.center(30))
print(spam.ljust(30))

print(' Hello '.rjust(30, '*'))
print(' Hello '.center(30, '+'))
print('Hello '.ljust(30, '='))

""""Removing Whitespace with strip(), rstrip(), and lstrip()"""

spam = '     Hello World       ' 
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())


spam = '=======Hello World=======' 
print(spam.strip('='))
print(spam.lstrip('='))
print(spam.rstrip('='))

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
