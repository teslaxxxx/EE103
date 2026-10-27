x = 0

for i in range(10):
    x += 0.1

print("x =", x)
print("x == 1.0:", x == 1.0)

epsilon = 1e-10
print("Approximately equal:", abs(x - 1.0) < epsilon)