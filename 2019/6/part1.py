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

def count_orbits(tree, depth):
	count = len(tree.keys()) * depth
	for node in tree.values():
		count += count_orbits(node, depth+1)
	return count

links = [(x.split(')')[0], x.split(')')[1]) for x in open("input.txt").read().strip().split('\n')]
tree = dict()
tree['COM'] = dict()
planets = ['COM']
while planets != []:
	tree, planets = add_links(tree, sorted(links), planets)
print (count_orbits(tree, 0))