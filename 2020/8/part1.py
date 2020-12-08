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
		return acc
	if pos in history:
		return acc
	if pos >= len( code ):
		return acc
	line = code[pos].split()
	pos, history, acc = runOneLine( line, pos, history, acc )
	return runCode( code, pos, history, acc )

code = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( "Final acc: {}".format( runCode( code, 0, set(), 0 ) ) )
