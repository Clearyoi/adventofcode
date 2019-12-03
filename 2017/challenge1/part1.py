input = 1122
lastDigit = 0
total = 0
first = input % 10

while input > 0:
    digit = input % 10
    if digit == lastDigit:
        total += digit
    input /= 10
    lastDigit = digit

if lastDigit == first:
    total += first
print total
