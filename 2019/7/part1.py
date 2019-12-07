import sys
import itertools

def read_mem(mem, addr, mode, para):
	return mem[addr+para] if int(mode/(10**(para-1)))%10==1 else mem[mem[addr+para]]

def run_comp(automatic, inputs, output):
	mem = [int(x) for x in open("input.txt").read().strip().split(',')]
	i = 0
	input_index = 0
	while mem[i]:
		op = mem[i] % 100
		mode = int(mem[i] / 100)
		if op == 99:
			if not automatic:
				print('done')
			return output
		elif op == 1:
			mem[mem[i+3]] = read_mem(mem, i, mode, 1) + read_mem(mem, i, mode, 2)
			i += 4
		elif op == 2:
			mem[mem[i+3]] = read_mem(mem, i, mode, 1) * read_mem(mem, i, mode, 2)
			i += 4
		elif op == 3:
			if automatic:
				mem[mem[i+1]] = inputs[input_index]
				input_index += 1
			else:
				print('Enter input:')
				mem[mem[i+1]] = int(input())
			i += 2
		elif op == 4:
			output = read_mem(mem, i, mode, 1)
			if not automatic:
				print('output', output)
			i += 2
		elif op == 5:
			i = read_mem(mem, i, mode, 2) if read_mem(mem, i, mode, 1) != 0 else i + 3
		elif op == 6:
			i = read_mem(mem, i, mode, 2) if read_mem(mem, i, mode, 1) == 0 else i + 3
		elif op == 7:
			mem[mem[i+3]] = 1 if read_mem(mem, i, mode, 1) < read_mem(mem, i, mode, 2) else 0
			i += 4
		elif op == 8:
			mem[mem[i+3]] = 1 if read_mem(mem, i, mode, 1) == read_mem(mem, i, mode, 2) else 0
			i += 4
		else:
			print('err bad op')
			print(mem)
			print('op:', op, 'i', i)
			return output

max_sig = 0
for perm in list(itertools.permutations([0, 1, 2, 3, 4])):
	sig = 0
	sig = run_comp(True, [perm[0], sig], 'NO OUTPUT CREATED')
	sig = run_comp(True, [perm[1], sig], 'NO OUTPUT CREATED')
	sig = run_comp(True, [perm[2], sig], 'NO OUTPUT CREATED')
	sig = run_comp(True, [perm[3], sig], 'NO OUTPUT CREATED')
	sig = run_comp(True, [perm[4], sig], 'NO OUTPUT CREATED')
	if sig > max_sig:
		max_sig = sig

print(max_sig)
