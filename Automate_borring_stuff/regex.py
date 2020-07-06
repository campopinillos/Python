#!/usr/bin/env python3
"""Find a phone number using regular expression"""

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