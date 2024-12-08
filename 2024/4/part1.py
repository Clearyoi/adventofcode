import re
import numpy

def countLine(line):
	c = len(re.findall(r"XMAS", line))
	c += len(re.findall(r"SAMX", line))
	return c

def countDiag(line):
	s = ''
	for i in line:
		s += i
	return countLine(s)

def countDiags(lines, l):
	diagTotal = 0
	arr = numpy.array([list(x) for x in lines])
	line = numpy.diag(arr, 0)
	diagTotal += countDiag(line)
	for i in range(1,l):
		line = numpy.diag(arr, i)
		diagTotal += countDiag(line)
		line = numpy.diag(arr, -i)
		diagTotal += countDiag(line)
	return diagTotal

def getResult( lines ):
	total = 0
	newLines = []
	# it's a square so this is fine
	l = len(lines)
	for line in lines:
		total += countLine(line)
	for i in range(l):
		newLine = ''
		for j in range(l):
			newLine += lines[l-j-1][i]
		total += countLine(newLine)
		newLines.append(newLine)
	total += countDiags(lines, l)
	total += countDiags(newLines, l)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 18 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )