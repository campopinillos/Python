#!/usr/bin/env python3
def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        print(max_ending_here, max_so_far)
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


a = [1, -3, 2, -5, 7, 6, -1, -4, 11, -23]
b = maxSubArraySum(a, 10)
print(b)
