number = float(input("enter a number:"))

epsilon = 0.01
low = 0.0
high = max(1.0,number)
num_guesses = 0

guess = (low+high)/2

while abs(guess**2 - number)>= epsilon:
    if guess**2 < number:
        low = guess
    else:
        high = guess

    guess = (low+high)/2
    num_guesses +=1

print("Approximate square root:",guess)
print("number of guesses:", num_guesses)
print("Squared error:", abs(guess**2- number))

    