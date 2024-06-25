rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

row = 0
while row < rows:
    col = 0
    while col < cols:
        if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
            print('*', end='')
        else:
            print(' ', end='')
        col += 1
    print() 
    row += 1
