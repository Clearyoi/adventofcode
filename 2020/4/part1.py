def countValid( passports ):
	validCount = 0
	requiredFields = [ 'byr' , 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]
	for passport in passports:
		valid = True
		passport = passport.replace( '\n', ' ' )
		fields = passport.split()
		fieldNames = [ x.split( ':' )[0] for x in fields ]
		for req in requiredFields:
			if req not in fieldNames:
				valid = False
				continue
		if valid:
			validCount += 1
	return validCount

passports = [ x for x in open( "input.txt" ).read().strip().split( '\n\n' ) ]
print ( 'Number of valid passports: {}'.format( countValid( passports ) ) )
