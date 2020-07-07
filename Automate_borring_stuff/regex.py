#!/usr/bin/env python3
"""
Find a phone number using regular expression
Methods: seach, findall, group, groups
Symbols:
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
"""

import re

message = 'Call me 415-555-1234 tomorrow, or at 415-555-9999'
pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# To print first ocurrance
number = pattern.search(message)
print(number.group())

# To print all ocurrances
numbers = pattern.findall(message)
print(numbers)

# Working with groups
# Same Example with number
message = 'Call me 415-555-1234 tomorrow, or at 415-555-9999, and 321-555-1111'
pattern = re.compile(r'([\d]{3}-[\d]{3}-[\d]{4})')

# To print first ocurrance
number = pattern.search(message)
print(number.group())

# To print all ocurrances
numbers = pattern.findall(message)
print(numbers)

message = 'Call me 415-555-1234'
pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
numbers = pattern.search(message)
print(numbers.group())
print(numbers.group(1))
print(numbers.group(2))
print(numbers.groups())

# Note if you want to look for a parenthesis it is necesary to use \ backslash

message = 'Call me (415)-555-1234'
pattern = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
numbers = pattern.search(message)
print(numbers.group())
print(numbers.group(1))
print(numbers.group(2))
print(numbers.groups())

# Matching Multiple Groups with the Pipe

message = "Batmobile lost a wheel"
pattern = re.compile(r'Bat(man|copter|mobile)')
mo = pattern.search(message)
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.groups())

# Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())


# Matching Zero or More with the Star

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())

# Matching One or More with the Plus

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batman') == None
print(mo1)
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())

# The caret and dollar Sign characters
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!').group())

endsWithWorld = re.compile(r'World!$')
print(endsWithWorld.search('Hello World!').group())
print(endsWithWorld.findall('Hello World!'))
print(endsWithWorld.findall('Hello World!')[0])

allDigits = re.compile(r'^\d+$')
print(allDigits.search('48917981237').group())
print(allDigits.search('489179d81237') == None)

# The wildcard character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
atRegex = re.compile(r'.{1,2}?at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Matching Everything with Dot-Star .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Alan23144 Last Name: Sweigart2132')
print(mo.group(1))
print(mo.group(2))

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# Case-insensitive matching
robocop = re.compile(r'robocop', re.I) # re.IGNORECASE for non case sensitive
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

"""Substituting Strings with the sub() method"""
message = 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', message))

# Use \num backslash number to replace by group
message = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'Agent \1*****', message))
