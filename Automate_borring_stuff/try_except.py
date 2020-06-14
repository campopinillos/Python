#!/usr/bin/python3
'''Try and Except'''

def div42by(divideby):
	try:
		return 42 / divideby
	except ZeroDivisionError:
		print('Error')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
