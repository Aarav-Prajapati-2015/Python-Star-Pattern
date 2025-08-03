for row in range(1, 8):
    for col in range(1, 8):
        if (col==1) or (row==7):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()