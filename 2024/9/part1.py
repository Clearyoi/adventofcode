def setupMemory(lines):
	memory = []
	index = 0
	for i,x in enumerate(lines):
		if i % 2 == 0:
			memory += [index]*x
			index += 1
		else:
			memory += [-1]*x
	return memory

def swapMem(memory):
	lastFull, firstEmpty, val = 0,0, -2
	for i in reversed(range(len(memory))):
		if memory[i] != -1:
			lastFull = i
			break
	for i, m in enumerate(memory):
		if m == -1:
			firstEmpty = i
			val = m
			break
	if lastFull < firstEmpty:
		return memory
	memory[firstEmpty] = memory[lastFull]
	memory[lastFull] = -1
	return memory


def compactMemory(memory):
	freeMem = len([x for x in memory if x==-1])
	for i in range(freeMem-1):
		memory = swapMem(memory)
	return memory

def countMemory(memory):
	total = 0
	for i,m in enumerate(memory):
		if m == -1:
			break
		total += i*m
	return total

def getResult( lines ):
	memory = setupMemory(lines)
	memory = compactMemory(memory)
	return countMemory(memory)

def readData( filename ):
	return [int(x) for x in list(open( filename ).read().strip()) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 1928 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
