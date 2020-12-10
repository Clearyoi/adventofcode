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

def findWeakRange( nums, chunkSize ):
	invalidNum = findFirstUnmatchedNum( nums, chunkSize )
	for i, num in enumerate( nums ):
		weakRange = [num]
		for n in nums[i+1:]:
			weakRange.append( n )
			if sum( weakRange ) == invalidNum:
				return weakRange
			if sum( weakRange ) > invalidNum:
				break

def findEncyptionWeakness( nums, chunkSize ):
	weakRange = findWeakRange( nums, chunkSize )
	return min( weakRange ) + max( weakRange )

nums = [ int( x ) for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("Encyption Weakness: {}".format( findEncyptionWeakness( nums, 25 ) ) )
