input_text = open("./day2.txt").read()

# input_text = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

def is_any_subsequence_safe(sequence):
	for i in range(len(sequence)):
		sub_sequence = sequence[:i] + sequence[i+1:]
		if is_line_safe(sub_sequence):
			return 1
	return 0

def is_line_safe(numbers, flexible=False):
	""" Returns 1 if the numbers on a line are safe, 0 otherwise 
	If flexible is True, allows to remove one element from numbers to consider the line safe 
	"""
	sequence = [int(i) for i in numbers]
	if sequence != sorted(sequence) and sequence != sorted(sequence, reverse=True):
		if not flexible:
			return 0
		elif not is_any_subsequence_safe(sequence):
			return 0
	preceding = None
	for n in sequence:
		if preceding:
			diff = abs(n - preceding)
			if diff > 3 or diff < 1:
				if not flexible:
					return 0
				elif not is_any_subsequence_safe(sequence):
					return 0
		preceding = n
	return 1

safe_cnt = sum(
	is_line_safe(line.split(' '))
	for line in input_text.split('\n')
)

print(safe_cnt)

# Part 2

safe_cnt = sum(
	is_line_safe(line.split(' '), flexible=True)
	for line in input_text.split('\n')
)

print(safe_cnt)



