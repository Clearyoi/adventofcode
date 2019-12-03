def fuel(mass):
	base = int(mass/3) - 2
	if base <= 0:
		return 0
	return base + fuel(base)

print(sum(fuel(int(x)) for x in open("input.txt").read().strip().split('\n')))