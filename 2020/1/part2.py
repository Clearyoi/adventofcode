def findPair( goal, nums ):
	if len( nums ) < 2:
		return 0, False
	head = nums[0]
	if goal - head in nums[1:]:
		return head * (goal - head), True
	return findPair( goal, nums[1:] )

def findTriplet( goal, nums ):
	if len( nums ) < 3:
		return 0, False
	head = nums[0]
	partial, success = findPair( goal - head, nums[1:] )
	if success:
		return head * partial, True
	return findTriplet( goal, nums[1:] )

nums = [ int( x ) for x in open( "input.txt" ).read().strip().split( '\n' ) ]
result, success = findTriplet( 2020, nums )
if success:
	print( result )
else:
	print( 'no triplet found' )