import re


def countValid( passports ):
	validCount = 0
	for passport in passports:
		valid = True
		passport = passport.replace( '\n', ' ' )
		fields = passport.split()
		ppData = [ x.split( ':' ) for x in fields ]
		if not validateByr( ppData ):
			continue
		if not validateIyr( ppData ):
			continue
		if not validateEyr( ppData ):
			continue
		if not validateHgt( ppData ):
			continue
		if not validateHcl( ppData ):
			continue
		if not validateEcl( ppData ):
			continue
		if not validatePid( ppData ):
			continue
		validCount += 1
	return validCount

def validateByr( ppData ):
	for field in ppData:
		if field[0] == 'byr':
			if int(field[1]) >= 1920 and int(field[1]) <= 2002:
				return True
	return False

def validateIyr( ppData ):
	for field in ppData:
		if field[0] == 'iyr':
			if int(field[1]) >= 2010 and int(field[1]) <= 2020:
				return True
	return False

def validateEyr( ppData ):
	for field in ppData:
		if field[0] == 'eyr':
			if int(field[1]) >= 2020 and int(field[1]) <= 2030:
				return True
	return False

def validateHgt( ppData ):
	for field in ppData:
		if field[0] == 'hgt':
			for i,c in enumerate( field[1] ):
			    if not c.isdigit():
			        break
			value = int( field[1][:i] )
			unit = field[1][i:]
			if unit == 'cm' and value >= 150 and value <= 193:
				return True
			if unit == 'in' and value >= 59 and value <= 76:
				return True
	return False

def validateHcl( ppData ):
	for field in ppData:
		if field[0] == 'hcl':
			if re.match( r'\#([0-9a-f]){6}', field[1] ):
				return True
	return False

def validateEcl( ppData ):
	validEyeColours = [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]
	for field in ppData:
		if field[0] == 'ecl':
			if field[1] in validEyeColours:
				return True
	return False

def validatePid( ppData ):
	for field in ppData:
		if field[0] == 'pid':
			if len( field[1] ) == 9 and re.match( r'([0-9]){9}', field[1] ):
				return True
	return False


passports = [ x for x in open( "input.txt" ).read().strip().split( '\n\n' ) ]
print ( 'Number of valid passports: {}'.format( countValid( passports ) ) )
