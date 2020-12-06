def overallTotal( groups ):
	return sum ( [ groupTotal( group ) for group in groups ] )

def groupTotal( group ):
	group = group.replace( '\n' , '')
	answers = set()
	for answer in group:
		answers.add( answer )
	return len( answers )

groups = [ x for x in open( "input.txt" ).read().strip().split( '\n\n' ) ]
print( 'Total: {}'.format( overallTotal ( groups ) ) )