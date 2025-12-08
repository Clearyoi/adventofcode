import math

class box:
	def __init__(self, id, x, y, z):
		self.id = id
		self.x = x
		self.y = y
		self.z = z
		self.dists = []
		self.connected = []

	def calcDists(self, boxes):
		for b in boxes:
			if b.id == self.id:
				continue
			dist = math.sqrt(((self.x-b.x)*(self.x-b.x))+((self.y-b.y)*(self.y-b.y))+((self.z-b.z)*(self.z-b.z)))
			self.dists.append((dist, b.id))
		self.dists.sort()

	def nextClosest(self):
		for d in self.dists:
			if d[1] not in self.connected:
				return d

	def prettyPrint(self):
		print(f"{self.id}: {self.x}, {self.y}, {self.z}:  [{self.connected}]")
			

def getResult( lines, conn ):
	total = 0
	boxes = []
	groups = []
	for i, line in enumerate(lines):
		vals = line.split(",")
		b = box(i, int(vals[0]),int(vals[1]),int(vals[2]))
		boxes.append(b)
		groups.append([b.id])
	for b in boxes:
		b.calcDists(boxes)
	for i in range(conn):
		shortest = (9999999999, 0, 0)
		for b in boxes:
			c = b.nextClosest()
			if c[0] < shortest[0]:
				shortest = (c[0], c[1], b.id)
		# print(f"connecting {shortest[1]}:{shortest[2]}")
		boxes[shortest[1]].connected.append(shortest[2])
		boxes[shortest[2]].connected.append(shortest[1])
		g1, g2 = 0, 0
		for j, g in enumerate(groups):
			if shortest[1] in g:
				g1 = j
			if shortest[2] in g:
				g2 = j
		if g1 != g2:
			for v in groups[g2]:
				groups[g1].append(v)
			del groups[g2]

	groupLens = []
	for g in groups:
		groupLens.append(len(g))
	groupLens.sort(reverse=True)
	total = groupLens[0] * groupLens[1] * groupLens[2]
	# for b in boxes:
	# 	b.prettyPrint()
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, conn, expected ):
	result = getResult( testData, conn )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 10, 40 ):
	print( getResult( readData( "input.txt" ), 1000 ) )
	print( "Done" )