#!/usr/bin/env python3
'''This program counts the letters in a message pass to it'''
import pprint
import sys

# Prueba 'It was a bright cold day in April, and the clock were striking thirteen.'
input = sys.argv[1]
message = "".join(input.split()) # Removing spaces
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count) # Pretty
rjtex = pprint.pformat(count)
print(rjtex)
