input = "1212"
length = len(input)
total = 0
pos = 0
for digit in input:
    if digit == input[((length/2) + pos) % length]:
        total += int(digit)
    pos += 1

print total
