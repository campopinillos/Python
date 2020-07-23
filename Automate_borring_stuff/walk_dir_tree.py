#!/usr/bin/env python3
"""
Scripts that receives a path and walk through a directory tree
"""
import os
import sys

path = sys.argv[1]

# for folderName, subfolder, filename in owalk(path):
# 	print('Folder' + folderName)
# 	print('Subfolder' + str(subfolder))
# 	print('Files' + str(filename))
	

for folderName, subfolders, filenames in os.walk(path):
	
	print('Current Folder: ' + folderName.center(len(path) + 10, '*'))
	
	for subfolder in subfolders:
		print('Subfolder of: ' + os.path.relpath(folderName) + ': ' + subfolder.center(len(path), '+'))
	
	for filename in filenames:
		print('File Inside: ' + os.path.relpath(folderName) + ': '.ljust(len(path) - 20, '.') + filename.rjust(25))
	print('')