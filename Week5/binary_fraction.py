number = 0.1

fraction = number
binary_fraction = ""
result = 0.0

epsilon = 0.00001
position = 1

while abs(result - number) >= epsilon and position <= 64:

    fraction *= 2

    bit = int(fraction)

    binary_fraction += str(bit)

    result += bit * 2**(-position)

    fraction -= bit

    position += 1

print("Binary:", "0." + binary_fraction)
print("Approximation:", result)
print("Error:", abs(result - number))
print("Bits used:", len(binary_fraction))