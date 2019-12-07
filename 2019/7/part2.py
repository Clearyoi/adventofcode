import sys
import itertools

def read_mem(mem, addr, mode, para):
	return mem[addr+para] if int(mode/(10**(para-1)))%10==1 else mem[mem[addr+para]]

def run_comp(mem, automatic, inst, inputs, output):
	i = inst
	# sick hacks
	input_index = 0 if i == 0 else 1
	while mem[i]:
		op = mem[i] % 100
		mode = int(mem[i] / 100)
		if op == 99:
			if not automatic:
				print('done')
			return output, mem, -1
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
				print('output:', output)
			i += 2
			if automatic:
				return output, mem, i
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
			return output, mem, -2

starting_mem = [int(x) for x in open("input.txt").read().strip().split(',')]
max_sig = 0
for perm in list(itertools.permutations([5, 6, 7, 8, 9])):
	sig, insta, instb, instc, instd, inste = 0, 0, 0, 0, 0, 0
	mema, memb, memc, memd, meme = starting_mem, starting_mem, starting_mem, starting_mem, starting_mem
	while insta >= 0:
		sig, mema, insta = run_comp(mema, True, insta, [perm[0], sig], sig)
		sig, memb, instb = run_comp(memb, True, instb, [perm[1], sig], sig)
		sig, memc, instc = run_comp(memc, True, instc, [perm[2], sig], sig)
		sig, memd, instd = run_comp(memd, True, instd, [perm[3], sig], sig)
		sig, meme, inste = run_comp(meme, True, inste, [perm[4], sig], sig)
	if sig > max_sig:
		max_sig = sig

print(max_sig)
