#!/usr/bin/env python3
"""List Methods"""

spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']

# Returns the index of the FIRST element with the specified value
spam.index('hi')

# Adds an element at the end of the list
spam.append('how r u')
print(spam)

# Add the elements of a list (or any iterable), to the end of the current list
spam.extend('heya')
print(spam)


# Adds an element at the specified position
spam.insert(1, 'hey')
print(spam)

# Removes the FIRST item with the specified value
spam.remove('hi')
print(spam)

# Delete by index
del spam[0]
print(spam)

# Removes the item at a specific index and returns it
spam.pop(4)  # Removes the element at the specified position
print(spam)

spam.pop()
spam.pop()
spam.pop()
spam.pop()
print(spam)

# Removes all the elements from the list
spam.clear()
print(spam)


# Returns the number of elements
spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
print(len(spam))

# Returns the number of elements with the specified value
print(spam.count('hi'))

# Sorts the list
spam = ['dogs', 'ants', 'cats', 'elephants', 'badgers']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

# ASCII Order
spam = ['A', 'B', 'a', 'c', 'D', 'C', 'b', 'd']
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)

# To extend the list with another list
spam.extend(['E', 'e'])
print(spam)

# Reverses the order of the list
spam.reverse()
print(spam)


# Returns a copy of the list
spam = ['dogs', 'ants', 'cats', 'elephants', 'badgers']

# If don't use copy it affects the original list
eggs = spam
print(eggs)
print(spam)

eggs.pop()
print(eggs)
print(spam)

# Proper way to copy
spam = ['dogs', 'ants', 'cats', 'elephants', 'badgers']
eggs = spam.copy() #  this also works    eggs = spam[:]
print(eggs)
print(spam)

eggs.pop()
print(eggs)
print(spam)
