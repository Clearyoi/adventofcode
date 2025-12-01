def setupMemory(lines):
	files = dict()
	freeMem = dict()
	fileId, memIndex = 0,0
	for i,x in enumerate(lines):
		if i % 2 == 0:
			files[memIndex] = (x, fileId)
			fileId += 1 
		else:
			freeMem[memIndex] = x
		memIndex += x
	return files, freeMem

def moveFile(files, freeMem, fileLoc):
	for i in sorted(freeMem.keys()):
		if i > fileLoc:
			break
		f = freeMem[i]
		fileSize = files[fileLoc][0]
		fileId = files[fileLoc][1]
		if f >= fileSize:
			files[i] = files[fileLoc]
			files.pop(fileLoc)
			freeMem[i+fileSize] = f-fileSize
			freeMem.pop(i)
			break
	return files, freeMem


def compactMemory(files, freeMem):
	fileList = list(files.keys())
	fileList.reverse()
	for fl in fileList:
		files, freeMem = moveFile(files, freeMem, fl)
	return files

def countMemory(memory):
	total = 0
	for i,m in enumerate(memory):
		if m == '.':
			continue
		total += i*int(m)
	return total

def compileMemory(files, memLen):
	output = ["."]*memLen
	for i in sorted(files.keys()):
		m = files[i]
		for j in range(m[0]):
			output[i+j] = str(m[1])
	return output

def getResult( lines ):
	files, freeMem = setupMemory(lines)
	files = compactMemory(files, freeMem)
	finalMem = compileMemory(files, 100000) #magic
	return countMemory(finalMem)

def readData( filename ):
	return [int(x) for x in list(open( filename ).read().strip()) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 2858 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
