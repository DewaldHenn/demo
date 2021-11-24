

for x in range(0,9):
    for y in range((9 - x) - 1):
        print(end=" ")

    for y in range(x + 1):
        print("*", end=" ")
    print()
