import sys

def dist(x, y):
	return abs(x) + abs(y)

def process(route, inst, xpos, ypos, steps):
	if (inst[0]) == 'U':
		for y in range(ypos, ypos+int(inst[1:])):
			steps += 1
			dst = dist(xpos, y)
			if dst in route.keys():
				if (xpos, y) not in route[dst]:
					route[dst][(xpos, y)] = steps
			else:
				route[dst] = dict()
				route[dst][(xpos, y)] = steps
		ypos += int(inst[1:])
	if (inst[0]) == 'D':
		for y in range(ypos, ypos-int(inst[1:]), -1):
			steps += 1
			dst = dist(xpos, y)
			if dst in route.keys():
				if (xpos, y) not in route[dst]:
					route[dst][(xpos, y)] = steps
			else:
				route[dst] = dict()
				route[dst][(xpos, y)] = steps
		ypos -= int(inst[1:])
	if (inst[0]) == 'R':
		for x in range(xpos, xpos+int(inst[1:])):
			steps += 1
			dst = dist(x, ypos)
			if dst in route.keys():
				if (x, ypos) not in route[dst]:
					route[dst][(x, ypos)] = steps
			else:
				route[dst] = dict()
				route[dst][(x, ypos)] = steps
		xpos += int(inst[1:])
	if (inst[0]) == 'L':
		for x in range(xpos, xpos-int(inst[1:]), -1):
			steps += 1
			dst = dist(x, ypos)
			if dst in route.keys():
				if (x, ypos) not in route[dst]:
					route[dst][(x, ypos)] = steps
			else:
				route[dst] = dict()
				route[dst][(x, ypos)] = steps
		xpos -= int(inst[1:])
	return route, xpos, ypos, steps

def trace(x):
	route = dict()
	xpos, ypos, steps = 0, 0, -1
	for inst in x.split(','):
		route, xpos, ypos, steps = process(route, inst, xpos, ypos, steps) 
	return route

output = dict()
lines = [trace(x) for x in open("input.txt").read().strip().split('\n')]
for key in sorted(lines[0].keys()):
	if key > 0  and key in lines[1].keys():
		for pos in lines[0][key].keys():
			if pos in sorted(lines[1][key].keys()):
				output[lines[0][key][pos] + lines[1][key][pos]] = (pos, key)

answer = min(output.keys())
print ('answer ', answer)
print ('pos', output[answer][0])
print ('dst', output[answer][1])
