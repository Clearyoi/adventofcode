def getSeatID( seat ):
	seat = seat.replace( 'F', '0' )
	seat = seat.replace( 'B', '1' )
	seat = seat.replace( 'L', '0' )
	seat = seat.replace( 'R', '1' )
	return int( seat, 2 )


def getMaxID( boardingPasses ):
	seats = sorted( [ getSeatID( x ) for x in boardingPasses ] )
	return [ x for x in range( seats[0], seats[-1] + 1 ) if x not in seats ][0]

boardingPasses = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print('My seat is {}'.format( getMaxID( boardingPasses ) ) )