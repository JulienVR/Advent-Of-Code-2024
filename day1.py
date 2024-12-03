input_text = open("./day1.txt").read()

# input_text = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

x, y = list(), list()
for line in input_text.split("\n"):
	l1, l2 = line.split('   ')
	x.append(int(l1))
	y.append(int(l2))

# Part 1s

x.sort()
y.sort()

diff = sum(abs(x[i] - y[i]) for i in range(len(x)))
print(diff)

# Part 2

from collections import defaultdict
y_map = defaultdict(lambda: 0)
for y_i in y:
	y_map[y_i] += 1

score = sum(x_i * y_map[x_i] for x_i in x)
print(score)
