#rows = int(input("Row: "))
#for i in range(0, rows + 1):
#    for j in range(i):
#        print("*", end=" ")
#    print()


rows = int(input("Row: "))

for relax in range(rows, 1, -1):
    for lang in range(relax):
        print("*", end="")
    print()

if rows > 1: 
    print("*" + " " * (rows - 2) + "*")

for relax in range(2, rows + 1):
    for lang in range(relax):
        print("*", end="")
    print()

