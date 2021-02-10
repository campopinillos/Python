#!/usr/bin/env python3

a = 0
for a in range(5):
	if (a == 3):
		break
	if (a > 0):
		print(a)

a = 0
while a < 5:
	print(a)
	a += 1

a = 0
while True:
	print(a)
	a += 1
	if (a == 6):
		break

import random
a = random.randint(1, 10)
print(a)