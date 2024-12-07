import time

input_text = open("./day7.txt").read()

# input_text = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

class StopTraversal(Exception):
	# Allows to divide by 2 the time to process the data set
	pass

def traverse_tree(subtotal, target, numbers):
	""" Recursively traverse the tree of all possible subtotals

	Args:
		target: target value
		numbers: list of values to be used to try to reach the target 

	Returns:
		True if one final subtotal equals the target value
	"""
	if not numbers:
		return subtotal == target
	else:
		n = numbers[0]
		numbers = numbers[1:]
		is_left_target = traverse_tree((subtotal or 0) + n, target, numbers)
		# if is_left_target:
		# 	raise StopTraversal()
		is_mid_target = traverse_tree(int(str(subtotal or '') + str(n)), target, numbers)  # only useful for part 2
		# if is_mid_target:
		#	raise StopTraversal()
		is_right_target = traverse_tree((subtotal or 1) * n, target, numbers)
		# if is_right_target:
		#	raise StopTraversal()
		return is_left_target or is_mid_target or is_right_target

start = time.time()

tot_count = 0
for line in input_text.split('\n'):
	subtotals = []
	target, numbers_text = line.split(': ')
	target = int(target)
	numbers = [int(i) for i in numbers_text.split(' ')]
	if traverse_tree(None, target, numbers):
		tot_count += target

end = time.time()
print("Found:", tot_count, "in", round(end-start, 3), "sec")
