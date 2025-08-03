for row in range(1, 6):
    for col in range(1, 4):
        if (col==1) or (col==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()