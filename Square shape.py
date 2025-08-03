for row in range(1, 5):
    for col in range(1, 5):
        if (col==1) or (col==4) or (row==1) or (row==4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()