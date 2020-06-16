#!/usr/bin/env python3
"""Script to measure discance between points.
Example of a mean distance between 3 points or coords"""

import math


def dist(x1, y1, x2, y2):
    """Function to measure discance between points or coords"""
    dis = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
    return dis


# Distance Example
x1, y1, x2, y2, x3, y3 = 1, 1, 2, 2, 3, 3

dis1 = dist(x1, y1, x2, y2)
dis2 = dist(x3, y3, x2, y2)
dis3 = dist(x1, y1, x3, y3)

mean_distance = (dis1+dis2+dis3)/3
