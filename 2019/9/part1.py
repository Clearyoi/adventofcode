import sys
import itertools


def read_mem(mem, addr, rel, mode, para):
	type = int(mode/(10**(para-1)))%10
	if type == 1:
		return mem[addr+para]
	if type == 2:
		return mem[mem[addr+para] + rel] 
	else:
		return mem[mem[addr+para]]

def write_mem(mem, addr, rel, mode, para, val):
	type = int(mode/(10**(para-1)))%10
	if type == 1:
		print ('wtf does this mean?')
	if type == 2:
		mem[mem[addr+para] + rel] = val
	else:
		mem[mem[addr+para]] = val

def run_comp(mem, automatic, inst, rel, inputs, output):
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
			write_mem(mem, i, rel, mode, 3, read_mem(mem, i, rel, mode, 1) + read_mem(mem, i, rel, mode, 2))
			i += 4
		elif op == 2:
			write_mem(mem, i, rel, mode, 3, read_mem(mem, i, rel, mode, 1) * read_mem(mem, i, rel, mode, 2))
			i += 4
		elif op == 3:
			if automatic:
				write_mem(mem, i, rel, mode, 1, inputs[input_index])
				input_index += 1
			else:
				print('Enter input:')
				write_mem(mem, i, rel, mode, 1, int(input()))
			i += 2
		elif op == 4:
			output = read_mem(mem, i, rel, mode, 1)
			if not automatic:
				print('output:', output)
			i += 2
			if automatic:
				return output, mem, i
		elif op == 5:
			i = read_mem(mem, i, rel, mode, 2) if read_mem(mem, i, rel, mode, 1) != 0 else i + 3
		elif op == 6:
			i = read_mem(mem, i, rel, mode, 2) if read_mem(mem, i, rel, mode, 1) == 0 else i + 3
		elif op == 7:
			write_mem(mem, i, rel, mode, 3, 1 if read_mem(mem, i, rel, mode, 1) < read_mem(mem, i, rel, mode, 2) else 0)
			i += 4
		elif op == 8:
			write_mem(mem, i, rel, mode, 3, 1 if read_mem(mem, i, rel, mode, 1) == read_mem(mem, i, rel, mode, 2) else 0)
			i += 4
		elif op == 9:
			rel += read_mem(mem, i, rel, mode, 1)
			i += 2
		else:
			print('err bad op')
			print(mem)
			print('op:', op, 'i', i)
			return output, mem, -2

starting_mem = [int(x) for x in open("input.txt").read().strip().split(',')]
addr = 0
mem_as_dict = dict()
for addr_val in starting_mem:
	mem_as_dict[addr] = addr_val
	addr+=1
run_comp(mem_as_dict, False, 0, 0, [], 'default output')
