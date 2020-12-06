def overallTotal( groups ):
	return sum ( [ groupTotal( group ) for group in groups ] )

def groupTotal( group ):
	people = group.split( '\n' )
	answers = people[0]
	for person in people:
		for answer in answers:
			if answer not in person:
				answers = answers.replace( answer, '' )
	return len( answers )

groups = [ x for x in open( "input.txt" ).read().strip().split( '\n\n' ) ]
print( 'Total: {}'.format( overallTotal ( groups ) ) )