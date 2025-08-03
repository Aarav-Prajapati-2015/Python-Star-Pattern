for row in range(0,7):
    for col in range(0,5):
        if (col==2) or (row==0) or (col==1 and row==6) or (col==0 and row>3 and row<6) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()