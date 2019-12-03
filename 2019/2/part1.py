mem = [int(x) for x in open("input.txt").read().strip().split(',')]
mem[1] = 12
mem[2] = 2
i = 0
while mem[i]:
	if mem[i] == 99:
		print mem[0]
	elif mem[i] == 1:
		mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
	elif mem[i] == 2:
		mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
	else:
		print("err")
	i = i + 4