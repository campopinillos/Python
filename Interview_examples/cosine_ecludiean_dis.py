#!/usr/bin/env python3
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


def cosine(vector1, vector2):
  return np.dot(vector1, vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))

def euclidean(vector1, vector2):
  return np.sqrt(((np.linalg.norm(vector1 - vector2))*(np.linalg.norm(vector1 - vector2))))


vector1 = np.array([15, 5, 7, 1, 1, 0, 0, 1])
vector2 = np.array([1, 5, 7, 8, 8, 0, 0, 20])

print("cosine: ", cosine(vector1, vector2)) # 0.292919231098
print("euclidean: ", euclidean(vector1, vector2)) # 25.5929677841