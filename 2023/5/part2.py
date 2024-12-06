import re

def updateSeedList(seedList, section):
	# for ()
	return seedList

def createAlamanac(data):
	almanac = {}
	seeds, sections = data
	seeds = [int(x) for x in seeds[0].split()]
	seeds = list(zip(seeds[::2],seeds[1::2]))
	print('seeds', seeds)

def processResults(seeds, almanac):
	for seed in seeds:
		seedList = [seed[0], seed[1]]
		for section in almanac.keys():
			seedList = updateSeedList(seedList, section)
	return seeds, almanac

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
