def runOneLine( line, pos, history, acc ):
	history.add(pos)
	op, val = line[0], line[1]
	if op == 'nop':
		return pos + 1, history, acc
	if op == 'acc':
		return pos + 1, history, acc + int( val )
	if op == 'jmp':
		return pos + int( val ), history, acc 
	return pos, history, acc

def runCode( code, pos, history, acc ):
	if pos < 0:
		return False, acc
	if pos in history:
		return False, acc
	if pos >= len( code ):
		return True, acc
	line = code[pos].split()
	pos, history, acc = runOneLine( line, pos, history, acc )
	return runCode( code, pos, history, acc )

def repairCode( code ):
	pos, acc = 0, 0
	history = set()
	attemptedFixes = set()
	while True:
		line = code[pos].split()
		# If line has been changed before run unchanged
		if pos in attemptedFixes:
			pos, history, acc = runOneLine(line, pos, history, acc)
			continue

		# Take note of attempt
		attemptedFixes.add(pos)
		op, val = line[0], line[1]

		# Run acc unchanged 
		if op == 'acc':
			pos, history, acc = runOneLine(line, pos, history, acc)
			continue

		# Switch nop and jmp
		if op == 'nop':
			pos, history, acc  = runOneLine(['jmp', val], pos, history, acc)
		if op == 'jmp':
			pos, history, acc  = runOneLine(['nop', val], pos, history, acc)

		# Check if code terminates successfully
		result, final = runCode( code, pos, set(), acc )
		if result:
			return final

		# Reset if unsuccessful
		pos, acc = 0, 0
		history = set()


code = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( "Final acc: {}".format( repairCode( code ) ) )
