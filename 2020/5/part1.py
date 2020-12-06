def getSeatID( seat ):
	seat = seat.replace( 'F', '0' )
	seat = seat.replace( 'B', '1' )
	seat = seat.replace( 'L', '0' )
	seat = seat.replace( 'R', '1' )
	return int( seat, 2 )

def getMaxID( boardingPasses ):
	return max( [getSeatID( x ) for x in boardingPasses] )

boardingPasses = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print('The highest seat number is {}'.format( getMaxID( boardingPasses ) ) )