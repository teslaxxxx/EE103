low = 1
high = 148
num_guesses = 0

while low <= high:
    guess = (low+high) // 2
    num_guesses += 1

    print("My guess is :",guess)

    answer = input("Higher (h), lower(l), correct(c)?")

    if answer == "c":
        print("Found in", num_guesses, "guesses!")
        break
    elif answer == "h":
        low = guess +1

    elif answer == "l":
        high = guess-1

    else:
        print("please enter h,l,c.")
        num_guesses -= 1
else:
    print(" No page matches those hints.")