def valid(x):
	prev = -1
	pair = False
	lockPair = False
	justPaired = False
	for d in [int(d) for d in str(x)]:
		if d < prev:
			return False
		if d == prev:
			if justPaired and not lockPair:
				pair = False
			else:
				pair = True
				justPaired = True
		else:
			if pair and justPaired:
				lockPair = True
			justPaired = False
		prev = d
	return pair

limits = [int(x) for x in open("input.txt").read().strip().split('-')]
validNums = [x for x in range(limits[0], limits[1] + 1) if valid(x)]
print (len(validNums))