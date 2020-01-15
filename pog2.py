import random

x = 0
while x == 0:
	type = input('Army or Corps(c)?')
	if type == 'c':
		print('How many factors firing(after column shift for trench, swamp, mountains)?')
		column = int(input('Which column? 0, 1, 2, 3, 4, 5, 6, 7, 8+?'))
		drm = int(input('Any drm?'))
		roll = random.randint(1, 6)
		modified_roll = roll + int(drm)
		if modified_roll > 6:
			modified_roll = 6
		elif modified_roll < 1:
			modified_roll = 1
		print(f'Roll after modifiers: {modified_roll}')
		columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
		result = columns[column][column][modified_roll - 1]
		print(f'Table result: {result}')
		
	else:
		print('How many factors firing(after column shift for trench, swamp, mountains)?')
		column = int(input('Which column? 1, 2, 3, 4, 5, 6-8, 9-11, 12-14, 15, 16+?'))
		drm = int(input('Any drm?'))
		roll = random.randint(1, 6)
		modified_roll = roll + int(drm)
		if modified_roll > 6:
			modified_roll = 6
		elif modified_roll < 1:
			modified_roll = 1
		print(f'Roll after modifiers: {modified_roll}')
		columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
		result = columns[column][column][modified_roll - 1]
		print(f'Table result: {result}')