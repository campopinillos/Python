#!/usr/bin/env python3
"""Simple Calculator"""

import sys
import re


def calculator():
    operators = ['+', '-', '*', '/', '']
    Expression = input('(Press enter to exit)\nPlease put your operation:\n')
    pattern = re.compile(r'\s*')
    Expression = pattern.sub('', Expression)
    pattern = re.compile(r'(\d+)([-+/*])*')
    express = pattern.findall(Expression)
    if len(express) == 0:
        sys.exit(0)
    for i in express:
        if i[1] not in operators:
            print('Wrong operator')
            calculator()
    try:
        print(eval(Expression))
    except:
        print('Wrong input restate your expression')
    calculator()


calculator()
