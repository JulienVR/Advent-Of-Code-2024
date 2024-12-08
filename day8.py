import time
from collections import defaultdict

input_text = open("./day8.txt").read()

# input_text = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

parsed_input = [line.strip() for line in input_text.split('\n')]

antenna_coords = defaultdict(list)
for i in range(len(parsed_input)):
	for j in range(len(parsed_input[i])):
		if parsed_input[i][j] != '.':
			antenna_coords[parsed_input[i][j]].append((i, j))

def is_in_grid(i, j):
	return 0 <= i < len(parsed_input) and 0 <= j < len(parsed_input[i])

antinodes_coords = []
for antenna_type, coords_list in antenna_coords.items():
	# generate all possible pairs of antennas
	for i, antenna_1 in enumerate(coords_list):
		for antenna_2 in coords_list[i+1:]:
			antinodes_coords += [antenna_1, antenna_2]
			x_diff, y_diff = antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1]
			for func in int.__add__, int.__sub__:
				factor = 1
				while True:
					i, j = antenna_1 if func.__name__ == '__add__' else antenna_2
					antinode = func(i, factor * x_diff), func(j, factor * y_diff)
					if is_in_grid(*antinode):
						antinodes_coords.append(antinode)
						factor += 1
					else:
						break

def pprint():
	s = ''
	for i in range(len(parsed_input)):
		for j in range(len(parsed_input[i])):
			if parsed_input[i][j] == '.' and (i, j) in antinodes_coords:
				s += '#'
			else:
				s += parsed_input[i][j]
		s += '\n'
	print(s)

#pprint()
print(len(set(antinodes_coords)))
