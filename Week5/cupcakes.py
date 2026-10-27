total = 28

for david in range(total + 1):
    for emma in range(total + 1):
        for frank in range(total + 1):

            if (emma == david + 3 and
                frank == 3 * david and
                david + emma + frank == total):

                print("David packed", david, "cupcakes!")
                print("Emma packed", emma, "cupcakes!")
                print("Frank packed", frank, "cupcakes!")
