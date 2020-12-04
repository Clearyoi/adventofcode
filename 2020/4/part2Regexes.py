import re

def countValid( passports ):
    validations = [
    re.compile( r'byr:(20((0[0-9])|10)|19[2-9][0-9])(\s|$)' ),                  #byr
    re.compile( r'iyr:20(1[0-9]|20)(\s|$)' ),                                   #iyr
    re.compile( r'eyr:20(2[0-9]|30)(\s|$)' ),                                   #eyr
    re.compile( r'hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)(\s|$)' ),   #hgt
    re.compile( r'hcl:\#([0-9a-f]){6}(\s|$)' ),                                 #hcl
    re.compile( r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)' ),                   #ecl
    re.compile( r'pid:[0-9]{9}(\s|$)' ),                                        #pid
    ]
    validCount = 0
    for passport in passports:
        valid = True
        for validation in validations:
            if not validation.search ( passport ):
                valid = False
        if valid:
            validCount += 1
    return validCount


passports = [ x for x in open( "input.txt" ).read().strip().split( '\n\n' ) ]
print ( 'Number of valid passports: {}'.format( countValid( passports ) ) )