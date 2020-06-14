#!/usr/bin/python3
'''Interactive for loops'''

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

total = 0
for num in range(101):
    total = total + num
print(total)

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1

print('My name is')
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

print('My name is')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))
