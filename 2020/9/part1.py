def findFirstUnmatchedNum( nums, chunkSize ):
	for i, num in enumerate( nums ):
		if i <= chunkSize:
			continue
		if not validateNum( num, nums[i - chunkSize : i] ):
			return num
	return 0

def validateNum( num, preamble ):
	for n in preamble:
		if num - n in preamble:
			return True
	return False

nums = [ int( x ) for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("first invalid number: {}".format( findFirstUnmatchedNum( nums, 25 ) ) )
