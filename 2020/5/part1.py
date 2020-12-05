def getSeatID( seat ):
	seat = seat.replace( 'F', '0' )
	seat = seat.replace( 'B', '1' )
	seat = seat.replace( 'L', '0' )
	seat = seat.replace( 'R', '1' )
	row = int( seat[:7], 2 )
	col = int( seat[7:], 2 )
	return row * 8 + col

def getMaxID( boardingPasses ):
	return max( [getSeatID( x ) for x in boardingPasses] )

boardingPasses = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print('The highest seat number is {}'.format( getMaxID( boardingPasses ) ) )