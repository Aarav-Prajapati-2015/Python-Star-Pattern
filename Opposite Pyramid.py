# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# Code

num =  int(input("Enter the number of rows: "))

for row in range(1, num + 1):
    for space in range(row):
        print(" ", end=" ")
    for star in range(num - row):
        print("* ", end=" ")
    print()    
    