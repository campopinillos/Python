#!/usr/bin/env python3
"""
Working with paths and files
"""
import os
import shelve
import shutil
import send2trash

# Absolute path
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print('-----------------')

# Relative path
print(os.path.relpath('/Users/campopinillos', '/Users'))
print(os.path.relpath('/Users', '/Spam/Eggs'))

print('-----------------')

# Path, separator and files

path = os.getcwd() + '/files.py'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.sep)
print(path.split(os.path.sep))

print('-----------------')

# Checking current working directory and listing files
print(os.getcwd())
print(os.listdir())

print('-----------------')

# Checking size files and folders
path = os.getcwd()

print(os.path.getsize(path))
totalSize = 0
for filename in os.listdir(path):
	totalSize = totalSize + os.path.getsize(os.path.join(path, filename))
print(totalSize)

print('-----------------')

# Validating paths

print(os.path.exists('/Users'))
print(os.path.exists('/User'))
print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.path.isdir(path + '/files.py'))
print(os.path.isfile(path + '/files.py'))

print('-----------------')

# Saving Variables with the shelve module

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

with shelve.open('mydata1') as f:
	cats = ['Zophie', 'Pooka', 'Simon']
	f['cats'] = cats


# Manipulating files with shutil

# Copy and Move
with open('text.txt', 'w') as f:
	f.write('Hello World!')
shutil.copy('text.txt', 'spam.txt')
if 'text.txt' in os.listdir():
	shutil.move('text.txt', '..')
os.chdir('..')

for file in os.listdir():
	if file.endswith('.txt'):
		print(file)

# Delete and send to trash bin
send2trash.send2trash('text.txt')

os.chdir('./Automate_borring_stuff')

# Delete permanently
os.unlink('spam.txt')
os.unlink('mydata')
os.unlink('mydata1')
if os.path.exists('./__pycache__'):
	shutil.rmtree('./__pycache__')
print(os.getcwd())
if not os.path.exists('./test'):
	os.mkdir('test')
shutil.rmtree('./test')