def parseBags( bagsRaw ):
	bags = []
	for bag in bagsRaw:
		bags.append( ( bag[0].split()[0] + bag[0].split()[1], [ x.split()[1] + x.split()[2] for x in bag[1] ] ) )
	return bags
	
def findOuterBagsInner( bags, seeking ):
	newSeeking = seeking.copy()
	for bag in bags:
		for seek in seeking:
			if seek in bag[1]:
				newSeeking.add(bag[0])
	if newSeeking == seeking:
		return len(newSeeking) - 1
	return findOuterBagsInner( bags, newSeeking )

def findOuterBags( bagsRaw, goal ):
	bags = parseBags ( bagsRaw )
	seeking = set()
	seeking.add(goal)
	return findOuterBagsInner( bags, seeking )


bagsRaw = [ ( x.split( 'contain' )[0], x.split( 'contain' )[1].split( ',' ) )for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( "Number of bags which can contain my bag: {}".format( findOuterBags( bagsRaw, "shinygold" ) ) )
