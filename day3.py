import re
input_text = open("./day3.txt").read()

input_text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

s = 0
input_text = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", input_text, flags=re.DOTALL)
for m in re.findall("mul\(\d+,\d+\)", input_text):
	digits = re.findall("\d+", m)
	s += int(digits[0]) * int(digits[1])

print(s)
