#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:04:24 2020

@author: campopinillos
"""

# Use print("messages...") to debug your solution.
# Use print("messages...") to debug your solution.
from collections import namedtuple
import numpy as np


Dimensions = namedtuple("Dimensions", "columns rows")

def compute_product(matrixA, matrixB):
    matrixA_dim = Dimensions(len(matrixA[0]), len(matrixA))
    matrixB_dim = Dimensions(len(matrixB[0]), len(matrixB))
    product = []
    for col in range(matrixA_dim.rows):
        product.append([0 for row in range(matrixB_dim.columns)])
    for i in range(matrixA_dim.rows):
        for j in range(matrixB_dim.columns):
            product[i][j] = 0
            for k in range(matrixA_dim.columns):
                product[i][j] += (matrixA[i][k] * matrixB[k][j])
    return product

matrix_a = np.matrix('11, 3, 10, 3; 20, 1, 0, 1')
matrix_b = np.matrix('12, 1, 10; 7, 4, 0; 4, 5, 2; 5, 2, 10')

print("Product:")
print(compute_product(matrix_a, matrix_b))