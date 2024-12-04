input_text = open("./day4.txt").read()

# input_text = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

input_lines = input_text.split('\n')

def horizontal_range(i, j):
	return [
		[(i - d, j) for d in range(4)],
		[(i + d, j) for d in range(4)],
	]

def vertical_range(i, j):
	return [
		[(i, j - d) for d in range(4)],
		[(i, j + d) for d in range(4)],
	]

def diagonal_range(i, j):
	return [
		[(i + d, j + d) for d in range(4)],
		[(i + d, j - d) for d in range(4)],
		[(i - d, j + d) for d in range(4)],
		[(i - d, j - d) for d in range(4)],
	]

xmas_coords = []
for i in range(len(input_lines)):
	for j in range(len(input_lines[i])):
		if input_lines[i][j] == 'X':
			for coord_list in (horizontal_range(i, j) + vertical_range(i, j) + diagonal_range(i, j)):
				word = ''
				for x, y in coord_list:
					if not (0 <= x < len(input_lines)) or not (0 <= y < len(input_lines[x])):
						break
					word += input_lines[x][y]
				if word == 'XMAS':
					xmas_coords += [set(coord_list)]

# remove duplicate coordinates sequences
def remove_dup(xmas_coords):
	xmas_unique_coords = []
	for coords in xmas_coords:
		if coords not in xmas_unique_coords:
			xmas_unique_coords.append(coords)
	return xmas_unique_coords

print(len(remove_dup(xmas_coords)))

# Part 2

def part2_range(i, j):
	return [
		[(i + d, j + d) for d in (-1, 0, +1)],
		[(i + d, j - d) for d in (-1, 0, +1)],
	]

def read_letters(sequence):
	word = ''
	for x, y in sequence:
		if not (0 <= x < len(input_lines)) or not (0 <= y < len(input_lines[x])):
			break
		word += input_lines[x][y]
	return word

count_a = 0
xmas_coords = []
for i in range(len(input_lines)):
	for j in range(len(input_lines[i])):
		if input_lines[i][j] == 'A':
			words = []
			for sequence in part2_range(i, j):
				words.append(read_letters(sequence))
			if words[0] in ('SAM', 'MAS') and words[1] in ('SAM', 'MAS'):
				count_a += 1

print(count_a)
