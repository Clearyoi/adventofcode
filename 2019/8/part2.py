def read_row(pic, index, length):
	return [pic[index+i] for i in range(length)]

def read_layer(pic, index, length, height):
	return [read_row(pic, index+i*length, length) for i in range(height)]

def print_pixel(layers, i, j):
	for layer in layers:
		if int(layer[i][j]) == 0:
			print('  ', end = '')
			return
		if int(layer[i][j]) == 1:
			print('##', end = '')
			return
	print('err', layer[i][j])

pic = list(open("input.txt").read().strip())
layers = []
i = 0
while i < len(pic):
	layers.append(read_layer(pic, i, 25, 6))
	i += 25*6

for i in range(6):
	for j in range(25):
		print_pixel(layers, i, j)
	print('')
