
#!/usr/bin/env python3
"""
numpy matrix multiplication

Created on Mon Jan  6 13:28:09 2020

@author: campopinillos
"""
import numpy as np

matrix_a = np.matrix('11, 3, 10, 3; 20, 1, 0, 1')
matrix_b = np.matrix('12, 1, 10; 7, 4, 0; 4, 5, 2; 5, 2, 10')
np.matmul(matrix_a, matrix_b)

