#!/usr/bin/env python3
"""
Created on Mon Jan  6 14:16:50 2020

@author: campopinillos
"""

from math import sqrt
import numpy as np

def min_max_scaler(values):
    minvalue = min(values)
    denominator = max(values) - minvalue
    values_normalized = []
    for value in values:
        values_normalized.append((value - minvalue) / denominator)
    return values_normalized

def standardize(values):
    length_values = len(values)
    diffs = [value - np.mean(values) for value in values]
    std = sqrt(sum([diff**2 for diff in diffs]) / (length_values - 1))
    meanvalue = sum(values)/length_values
    values_standardized = []
    for value in values:
        values_standardized.append((value - meanvalue) / std)
    return values_standardized

values = [11, 30, 100, 41, 19, 0, 10, 55, 78, 90, -10, -11, 6, 105]
print("Normalized data:", min_max_scaler(values))
print("Standardize data:", standardize(values))