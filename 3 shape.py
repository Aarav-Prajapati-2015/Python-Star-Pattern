for row in range(1, 6):
    for col in range(1, 6):
        if (col==1) or (col==3) or (col==5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    