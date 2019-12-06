import sys
def tree_add(tree, parent, child):
	if parent in tree.keys():
		tree[parent][child] = dict()
		return tree, True
	else:
		for node in tree.keys():
			tree[node], added = tree_add(tree[node], parent, child)
			if added:
				return tree, True
	return tree, False

def add_links(tree, links, planets):
	new_planets = []
	for x in links:
		if x[0] in planets:
			new_planets.append(x[1])
			tree, added = tree_add(tree, x[0], x[1])
			if not added:
				print ('err', tree, x[0], x[1], planets)
				sys.exit()
	return tree, new_planets

def path_to_com_inner(pos, path, tree, x):
	if x == pos:
		return path, True
	path.append(pos)
	for node in tree.keys():
		path, finished = path_to_com_inner(node, path, tree[node], x)
		if finished:
			return path, finished
	return path[:-1], False

def path_to_com(tree, x):
	path, result = path_to_com_inner('>>', [], tree, x)
	if not result:
		print('uh oh')
	return path

def count_dist(path, planet):
	return path.index(planet)

def path_between(x, y):
	xpath = path_to_com(tree, x)
	xpath.reverse()
	ypath = path_to_com(tree, y)
	ypath.reverse()
	for planet in xpath:
		if planet in ypath:
			return count_dist(xpath, planet) + count_dist(ypath, planet)

links = [(x.split(')')[0], x.split(')')[1]) for x in open("input.txt").read().strip().split('\n')]
tree = dict()
tree['COM'] = dict()
planets = ['COM']
while planets != []:
	tree, planets = add_links(tree, sorted(links), planets)
print (path_between('YOU', 'SAN'))