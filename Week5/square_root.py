number = float(input("Enter a number: "))

epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - number) >= epsilon and guess**2 <= number:
    guess += increment
    num_guesses += 1

    if num_guesses % 1000000 == 0:
        print("Current guess =", guess)

print("Number of guesses:", num_guesses)
print("Approximate square root:", guess)

if abs(guess**2 - number) < epsilon:
    print("Approximation successful!")
else:
    print("Overshot the acceptable error range!")