def get_digit(num, i):
	digit = 0
	base_patern = [0, 1, 0, -1]
	for j in range(1, len(num)+1):
		# print (int(num[j-1]), '*', base_patern[int(j/i)%4], '+', end=' ')
		digit += int(num[j-1]) * base_patern[int(j/i)%4]
	# print('===', digit%10)
	return abs(digit) % 10


def perform_phase(num):
	out = []
	for i in range(1, len(num)+1):
		out.append(get_digit(num, i))
	return out

num = [x for x in open("input.txt").read().strip()]
for i in range(100):
	num = perform_phase(num)
for i in range(8):
	print(num[i], end='')
print('')