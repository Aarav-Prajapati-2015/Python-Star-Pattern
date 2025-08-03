for row in range(1, 8):
    for col in range(1, 8):
        if (col==4) or (row==1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()