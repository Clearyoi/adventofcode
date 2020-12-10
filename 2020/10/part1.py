def multiplyJolts( nums ):
	nums.append( 0 )
	nums = sorted( nums )
	ones, threes = 0, 1
	for i, num in enumerate( nums ):
		if i == 0:
			continue
		if num - nums[i-1] == 1:
			ones += 1
		if num - nums[i-1] == 3:
			threes += 1
	print (ones, threes)
	return ones * threes

nums = [ int( x ) for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("Answer: {}".format( multiplyJolts( nums ) ) )