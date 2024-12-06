import time

input_text = open("./day6.txt").read()

# input_text = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

class LoopFoundException(Exception):
	pass

# parse
input_map = [line for line in input_text.split('\n')]
for i in range(len(input_map)):
	for j in range(len(input_map[i])):
		if input_map[i][j] == '^':
			init_orientation, init_coords = '^', (i, j)

orientation = ['^', '>', 'v', '<']

added_obstacle = (-1, -1)

def is_obstacle(i, j):
	return (i, j) == added_obstacle or input_map[i][j] == '#'

def get_next_coords(i, j, orientation):
	""" Given coordinates i, j and the current orientation of the guard
	:returns: the next position of the guard and the list of visited nodes
	"""
	history = []
	i_prime, j_prime = i, j
	if orientation == '^':
		for i_prime in range(i, -1, -1):
			if is_obstacle(i_prime, j):
				return i_prime+1, j, history
			history.append((orientation, i_prime, j_prime))
	elif orientation == 'v':
		for i_prime in range(i, len(input_map)):
			if is_obstacle(i_prime, j):
				return i_prime-1, j, history
			history.append((orientation, i_prime, j_prime))
	elif orientation == '>':
		for j_prime in range(j, len(input_map[i])):
			if is_obstacle(i, j_prime):
				return i, j_prime-1, history
			history.append((orientation, i_prime, j_prime))
	else:
		for j_prime in range(j, -1, -1):
			if is_obstacle(i, j_prime):
				return i, j_prime+1, history
			history.append((orientation, i_prime, j_prime))
	return i_prime, j_prime, history

def traverse_map(i, j, guard_orientation):
	""" Traverse the map based on the initial coordinates of the guard and its orientation """
	history = []
	while True:
		i_start, j_start = i, j
		i, j, h = get_next_coords(i_start, j_start, guard_orientation)
		if h and h[0] in history:
			raise LoopFoundException()  # not great but I don't want to re-write this function ¯\_(ツ)_/¯
		history += h
		if (
			(i == len(input_map) - 1 and guard_orientation == 'v')
			or (i == 0 and guard_orientation == '^')
			or (j == len(input_map[i]) - 1 and guard_orientation == '>')
			or (j == 0 and guard_orientation == '<')
		):
			return history
		guard_orientation = orientation[(orientation.index(guard_orientation) + 1) % 4]

history = traverse_map(*init_coords, init_orientation)
visited_nodes = set((i, j) for _,i, j in history)

print("Number of visited nodes: ", len(visited_nodes))

# Part 2

start_time = time.time()
working_obstacles_count = 0
for node in visited_nodes - set(init_coords):
	# for each node traversed by the guard, add an obstacle...
	added_obstacle = node
	# ...and check if there's a loop in the traversal
	try:
		traverse_map(*init_coords, init_orientation)
	except LoopFoundException:
		working_obstacles_count += 1
end_time = time.time()
print("Number of worker obstacles: ", working_obstacles_count)
print("Part 2 took", round(end_time - start_time, 3), "sec")