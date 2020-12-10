def countArangements( nums ):
	start, count = 0, 1
	nums.append(0)
	nums = sorted( nums )
	for i, num in enumerate( nums ):
		if i == 0:
			continue
		if num - nums[i-1] == 3:
			count *= countSection( nums[start], nums[start+1:i] )
			start = i
	if start < len(nums) - 1:
		count *= countSection( nums[start], nums[start+1:] )
	return count

def countSection( start, nums ):
	if nums == []:
		return 1
	count = countSection( nums[0], nums[1:] )
	if len( nums ) >= 2 and nums[1] - start <= 3:
		count += countSection( nums[1], nums[2:] )
	if len( nums ) >= 3 and nums[2] - start <= 3:
		count += countSection( nums[2], nums[3:] ) 
	return count

nums = [ int( x ) for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("Answer: {}".format( countArangements( nums ) ) )