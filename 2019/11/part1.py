import sys
import itertools

class intComp:
	def __init__(self, starting_mem, automatic, default_output):
		self.mem = starting_mem
		self.addr = 0
		self.automatic = automatic
		self.rel = 0
		self.output = default_output

	def read_mem(self, mode, para):
		type = int(mode/(10**(para-1)))%10
		if type == 1:
			if self.addr+para in self.mem:
				return self.mem[self.addr+para]
			else:
				return 0
		if type == 2:
			if self.addr+para in self.mem:
				if self.mem[self.addr+para] + self.rel in self. mem:
					return self.mem[self.mem[self.addr+para] + self.rel] 
				else:
					return self.mem[0]
		else:
			if self.addr+para in self.mem:
				if self.mem[self.addr+para] in self.mem:
					return self.mem[self.mem[self.addr+para]]
				else:
					return self.mem[0]
			else:
				return 0

	def write_mem(self, mode, para, val):
		type = int(mode/(10**(para-1)))%10
		if type == 1:
			print ('wtf does this mean?')
		if type == 2:
			self.mem[self.mem[self.addr+para] + self.rel] = val
		else:
			self.mem[self.mem[self.addr+para]] = val

	def run_comp(self, inputs):
		input_index = 0
		while self.mem[self.addr]:
			op = self.mem[self.addr] % 100
			mode = int(self.mem[self.addr] / 100)
			if op == 99:
				if not self.automatic:
					print('done')
				return -1
			elif op == 1:
				self.write_mem(mode, 3, self.read_mem(mode, 1) + self.read_mem(mode, 2))
				self.addr += 4
			elif op == 2:
				self.write_mem(mode, 3, self.read_mem(mode, 1) * self.read_mem(mode, 2))
				self.addr += 4
			elif op == 3:
				if self.automatic:
					self.write_mem(mode, 1, inputs[input_index])
					input_index += 1
				else:
					print('Enter input:')
					self.write_mem(mode, 1, int(input()))
				self.addr += 2
			elif op == 4:
				self.output = self.read_mem(mode, 1)
				if not self.automatic:
					print('self.output:', self.output)
				self.addr += 2
				if self.automatic:
					return self.output
			elif op == 5:
				self.addr = self.read_mem(mode, 2) if self.read_mem(mode, 1) != 0 else self.addr + 3
			elif op == 6:
				self.addr = self.read_mem(mode, 2) if self.read_mem(mode, 1) == 0 else self.addr + 3
			elif op == 7:
				self.write_mem(mode, 3, 1 if self.read_mem(mode, 1) < self.read_mem(mode, 2) else 0)
				self.addr += 4
			elif op == 8:
				self.write_mem(mode, 3, 1 if self.read_mem(mode, 1) == self.read_mem(mode, 2) else 0)
				self.addr += 4
			elif op == 9:
				self.rel += self.read_mem(mode, 1)
				self.addr += 2
			else:
				print('err bad op')
				return -2

def move_forward(pos, direction):
	direction %= 4
	if direction == 0:
		return (pos[0], pos[1] + 1)
	if direction == 1:
		return (pos[0] + 1, pos[1])
	if direction == 2:
		return (pos[0], pos[1] - 1)
	if direction == 3:
		return (pos[0] - 1, pos[1])


starting_mem = [int(x) for x in open("input.txt").read().strip().split(',')]
addr = 0
mem_as_dict = dict()
for addr_val in starting_mem:
	mem_as_dict[addr] = addr_val
	addr+=1
painted = dict()
comp = intComp(mem_as_dict, True, 'default self.output')
action = 0
pos = (0, 0)
direction = 0
while action >= 0:
	# read current colour
	if pos in painted:
		current_colour = painted[pos]
	else:
		current_colour = 0
	# paint sqaure
	painted[(pos)] = comp.run_comp([current_colour])
	# turn robot
	action = comp.run_comp([current_colour])
	if action == 0:
		direction -= 1
	if action == 1:
		direction += 1
	# move forward
	pos = move_forward(pos, direction)
print(len(painted.keys()))


