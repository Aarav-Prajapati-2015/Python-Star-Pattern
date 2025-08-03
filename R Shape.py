for row in range(0, 7):
    for col in range(0, 5):
        if (col==0) or (col==4) and (row<4) or (row==0) or (row==3) or (col==1 and row==4) or (col==2 and row==5) or (col==3 and row==6):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()