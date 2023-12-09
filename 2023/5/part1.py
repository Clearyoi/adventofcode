import re

def createAlamanac(data):
	almanac = {}
	seeds, sections = data
	seeds = [int(x) for x in seeds[0].split()]
	for section in sections:
		lines = section[2].split('\n')
		sectionTransform = {}
		for line in lines:
			values = [int(x) for x in line.split()]
			sectionTransform[values[1]] = (values[1] + values[2], values[0] - values[1])
		almanac[(section[0],section[1])] = sectionTransform
	return seeds, almanac

def traverse(lookupType, lookupVal, almanac):
	if lookupType == 'location':
		return lookupVal
	for key in almanac.keys():
		if key[0] != lookupType:
			continue
		lookupType = key[1]
		matches = [x for x in almanac[key].keys() if x < lookupVal]
		match = -1
		if matches:
			match = max(matches)
		if match == -1:
			break	
		if almanac[key][match][0]<lookupVal:
			break
		lookupVal += almanac[key][match][1]
		break
	return traverse(lookupType, lookupVal, almanac)

def getResult( data ):
	results = []
	seeds, almanac = createAlamanac(data)
	for seed in seeds:
		results.append(traverse('seed', seed, almanac))
	return min(results)

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return (re.findall('seeds: ([^\n]*)', open( filename ).read(), re.S|re.M),
		[ x for x in re.findall(r'(\S*)-to-(\S*) map:\n(.*?)\n\n', open( filename ).read(), re.S|re.M)])

if runTest( readData( "input.tst" ), 35 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
