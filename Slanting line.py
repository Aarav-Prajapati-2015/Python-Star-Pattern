for row in range(0, 6):
    for col in range(0, 6):
        if (col==row):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()