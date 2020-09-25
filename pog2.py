import random

a_type = 'a'
loop = True


def normal(a_bonus, d_bonus, att_type, def_type, a_roll, d_roll, a_factor, d_factor):
	if att_type == 'a':
		a_columns(a_factor, a_roll, d_factor, d_roll, def_type)
	else:
		c_columns(a_factor, a_roll, d_factor, d_roll, def_type)

def flanking(a_bonus, d_bonus, att_type, def_type, a_roll, d_roll, a_factor, d_factor):
	if a_roll >= 4:
		print('Success!')
		if att_type == 'a':
			a_flanking_columns(a_factor, a_roll, d_factor, d_roll, def_type)
		else:
			c_flanking_columns(a_factor, a_roll, d_factor, d_roll, def_type)
	else:
		print('Failure!')
		if def_type == 'a':
			a_flanking_reversed_columns(d_factor, d_roll, a_factor, a_roll, att_type)
		else:
			c_flanking_reversed_columns(d_factor, d_roll, a_factor, a_roll, att_type)


def c_d_columns(d_factor, d_roll):
	columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
	print('Defender inflicts:')
	print(columns[d_factor][d_factor][d_roll - 1])

def a_d_columns(d_factor, d_roll):
	columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
	print('Defender inflicts:')
	print(columns[d_factor][d_factor][d_roll - 1])

def c_d_reversed_columns(d_factor, d_roll):
	columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
	print('Attacker inflicts:')
	print(columns[d_factor][d_factor][d_roll - 1])

def a_d_reversed_columns(d_factor, d_roll):
	columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
	print('Attacker inflicts:')
	print(columns[d_factor][d_factor][d_roll - 1])

def a_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
	print('Attacker inflicts:')
	print(columns[a_factor][a_factor][a_roll - 1])
	if def_type == 'c':
		c_d_columns(d_factor, d_roll)
	else:
		a_d_columns(d_factor, d_roll)

def c_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
	print('Attacker inflicts:')
	print(columns[a_factor][a_factor][a_roll - 1])
	if def_type == 'c':
		c_d_columns(d_factor, d_roll)
	else:
		a_d_columns(d_factor, d_roll)

def a_flanking_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
	print('Attacker inflicts:')
	result = columns[a_factor][a_factor][a_roll - 1]
	print(result)
	d_factor -= result
	if def_type == 'c':
		c_d_columns(d_factor, d_roll)
	else:
		a_d_columns(d_factor, d_roll)

def c_flanking_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
	print('Attacker inflicts:')
	result = columns[a_factor][a_factor][a_roll - 1]
	print(result)
	d_factor -= result
	if def_type == 'c':
		c_d_columns(d_factor, d_roll)
	else:
		a_d_columns(d_factor, d_roll)

def a_flanking_reversed_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[1,1]},{1:[0,1,1,1,2,2]}, {2:[1,1,2,2,3,3]}, {3:[1, 2, 2, 3, 3, 4]}, {4:[2, 2, 3, 3, 4, 4]}, {5:[2, 3, 3, 4, 4, 5]}, {6:[3, 3, 4, 4, 5, 5]},  {7:[3, 3, 4, 4, 5, 5]},  {8:[3, 3, 4, 4, 5, 5]}, {9:[3, 4, 4, 5, 5, 7]}, {10:[3, 4, 4, 5, 5, 7]},{11:[3, 4, 4, 5, 5, 7]}, {12:[4, 4, 5, 5, 7, 7]}, {13:[4, 4, 5, 5, 7, 7]}, {14 :[4, 4, 5, 5, 7, 7]}, {15 :[4, 5, 5, 7, 7, 7]}, {16 :[5, 5, 7, 7, 7, 7]}]
	print('Defender inflicts:')
	result = columns[a_factor][a_factor][a_roll - 1]
	print(result)
	d_factor = int(input('How many attacker factors still firing?'))
	if def_type == 'c':
		c_d_reversed_columns(d_factor, d_roll)
	else:
		a_d_reversed_columns(d_factor, d_roll)

def c_flanking_reversed_columns(a_factor, a_roll, d_factor, d_roll, def_type):
	columns = [{0:[0,0,0,0,1,1]},{1:[0,0,0,1,1,1]}, {2:[0,1,1,1,1,1]}, {3:[1, 1, 1, 1, 2, 2]}, {4:[1, 1, 1, 2, 2, 2]}, {5:[1, 1, 2, 2, 2, 3]}, {6:[1, 1, 2, 2, 3, 3]},  {7:[1, 2, 2, 3, 3, 4]},  {8:[2, 2, 3, 3, 4, 4]}]
	print('Defender inflicts:')
	result = columns[a_factor][a_factor][a_roll - 1]
	print(result)
	d_factor = int(input('How many attacker factors still firing?'))
	if def_type == 'c':
		c_d_reversed_columns(d_factor, d_roll)
	else:
		a_d_reversed_columns(d_factor, d_roll)


def roll(a_type):
	while (a_type != 'n') and (a_type != 'f'):
		a_type = input('Normal(n) or Flanking(f)?')
		a_bonus = int(input('Attacker DRM?'))
		d_bonus = int(input('Defender DRM?'))
		a_factor = int(input('Attacker factors firing?'))
		d_factor = int(input('Defender factors firing?'))
		att_type = input('Attacker type(a or c)?')
		def_type = input('Defender type(a or c)?')
		a_roll = random.randint(1, 6)
		d_roll = random.randint(1, 6)
		final_a_roll = a_roll + a_bonus
		if final_a_roll <= 0:
			final_a_roll = 1
		elif final_a_roll >= 6:
			final_a_roll = 6
		final_d_roll = d_roll + d_bonus
		if final_d_roll <= 0:
			final_d_roll = 1
		elif final_d_roll >= 6:
			final_d_roll = 6
		print(f'rolls are {final_a_roll} and {final_d_roll}')

		if a_type == 'n':
			normal(a_bonus, d_bonus, att_type, def_type, final_a_roll, final_d_roll, a_factor, d_factor)


		elif a_type == 'f':
			flanking(a_bonus, d_bonus, att_type, def_type, final_a_roll, final_d_roll, a_factor, d_factor)


while loop is True:
	roll(a_type)


