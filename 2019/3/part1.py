import sys

def dist(x, y):
	return abs(x) + abs(y)

def process(route, inst, xpos, ypos):
	if (inst[0]) == 'U':
		for y in range(ypos, ypos+int(inst[1:])):
			dst = dist(xpos, y)
			if dst in route.keys():
				route[dst].append((xpos, y))
			else:
				route[dst] = [(xpos, y)]
		ypos += int(inst[1:])
	if (inst[0]) == 'D':
		for y in range(ypos, ypos-int(inst[1:]), -1):
			dst = dist(xpos, y)
			if dst in route.keys():
				route[dst].append((xpos, y))
			else:
				route[dst] = [(xpos, y)]
		ypos -= int(inst[1:])
	if (inst[0]) == 'R':
		for x in range(xpos, xpos+int(inst[1:])):
			dst = dist(x, ypos)
			if dst in route.keys():
				route[dst].append((x, ypos))
			else:
				route[dst] = [(x, ypos)]
		xpos += int(inst[1:])
	if (inst[0]) == 'L':
		for x in range(xpos, xpos-int(inst[1:]), -1):
			dst = dist(x, ypos)
			if dst in route.keys():
				route[dst].append((x, ypos))
			else:
				route[dst] = [(x, ypos)]
		xpos -= int(inst[1:])
	return route, xpos, ypos

def trace(x):
	route = dict()
	xpos, ypos = 0, 0
	for inst in x.split(','):
		route, xpos, ypos = process(route, inst, xpos, ypos) 
	return route


lines = [trace(x) for x in open("input.txt").read().strip().split('\n')]
for key in sorted(lines[0].keys()):
	if key > 0  and key in lines[1].keys():
		for pos in lines[0][key]:
			if pos in sorted(lines[1][key]):
				print ('distance: ', key)
				print ('position: ', pos)
				sys.exit()

