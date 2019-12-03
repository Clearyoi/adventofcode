import sys

def run_comp(noun, verb): 
	mem = [int(x) for x in open("input.txt").read().strip().split(',')]
	mem[1] = noun
	mem[2] = verb
	i = 0
	while mem[i]:
		if mem[i] == 99:
			return mem[0]
		elif mem[i] == 1:
			mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
		elif mem[i] == 2:
			mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
		else:
			return -1
		i = i + 4

for i in range(0, 99):
	for j in range(0, 99):
		if run_comp(i, j) == 19690720:
			print 100 * i + j
			sys.exit()