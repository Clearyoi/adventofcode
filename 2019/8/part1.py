def count_digit(layer, digit):
	digits = 0
	for row in layer:
		for i in row:
			if int(i) == digit:
				digits += 1
	return digits

def one_times_twos(layer):
	print(count_digit(layer,2), count_digit(layer, 1), count_digit(layer, 2))
	return count_digit(layer, 1) * count_digit(layer, 2)

def read_row(pic, index, length):
	return [pic[index+i] for i in range(length)]

def read_layer(pic, index, length, height):
	return [read_row(pic, index+i*length, length) for i in range(height)]

pic = list(open("input.txt").read().strip())
layers = []
i = 0
while i < len(pic):
	layers.append(read_layer(pic, i, 25, 6))
	i += 25*6
min_zeros = 25*6+1
min_layer = []
for layer in layers:
	zeros = count_digit(layer, 0)
	print(zeros)
	if zeros < min_zeros:
		print('>', zeros, layer)
		min_zeros = zeros
		min_layer = layer

print(one_times_twos(min_layer))
