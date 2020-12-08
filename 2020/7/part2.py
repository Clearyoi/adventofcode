def parseBags( bagsRaw ):
	bags = []
	for bag in bagsRaw:
		bags.append( ( bag[0].split()[0] + bag[0].split()[1], [ (x.split()[0], x.split()[1] + x.split()[2] ) for x in bag[1] ] ) )
	return bags
	
def findInnerBagsInner( bags, goal ):
	count = 1
	for bag in bags:
		if goal == bag[0]:
			if bag [1][0][0] == 'no':
				return count
			for subBag in bag[1]:
				count += int( subBag[0] ) * findInnerBagsInner( bags, subBag[1] )
			return count
	return 1

def findInnerBags( bagsRaw, goal ):
	bags = parseBags ( bagsRaw )
	return findInnerBagsInner( bags, goal ) - 1


bagsRaw = [ ( x.split( 'contain' )[0], x.split( 'contain' )[1].split( ',' ) )for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( "Number of bags which my bag contains: {}".format( findInnerBags( bagsRaw, "shinygold" ) ) )
