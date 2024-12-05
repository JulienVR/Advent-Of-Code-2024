from collections import defaultdict

input_text = open("./day5.txt").read()

# input_text = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

rules = defaultdict(lambda: [])
updates = []

for line in input_text.split('\n'):
	if not line:
		continue
	if '|' in line:
		x, y = line.split('|')
		rules[int(x)].append(int(y))
	else:
		updates.append([int(i) for i in line.split(',')])

def is_update_correct(update):
	for i in range(len(update)):
		n = update[i]
		numbers_before = update[:i]
		if set(rules.get(n, [])).intersection(numbers_before):
			return False
	return True

median_sum = 0
for up in updates:
	if is_update_correct(up):
		median_sum += up[len(up)//2]
print(median_sum)

# Part 2

def get_correct_update(update):
	for i in range(len(update)):
		n = update[i]
		numbers_before = update[:i]
		fails = set(rules.get(n, [])).intersection(numbers_before)
		if fails:
			# exchange n and the rightmost failing number
			j = max(idx for idx in range(len(update)) if update[idx] in fails)
			new_update = update.copy()
			new_update[i], new_update[j] = new_update[j], new_update[i]
			# and repeat the process for the new update
			return get_correct_update(new_update)
	return update

median_sum = 0
for up in updates:
	correct_update = get_correct_update(up)
	if up != correct_update:
		median_sum += correct_update[len(correct_update)//2]
print(median_sum)
