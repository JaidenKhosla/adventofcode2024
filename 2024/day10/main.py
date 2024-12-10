
grid = None
with open("2024/day10/text.txt") as file:
    grid = [list(i) for i in file.read().strip().split('\n')]
    file.close()


score = 0

def navigate(row: int, col: int, listOfNines=set()):
    item = int(grid[row][col])
    if item == 9:
        listOfNines.add((row,col))
        return
    
    vertical = (row-1, row+1)
    horizontal = (col-1, col+1)
    for mutatedRow in vertical:
        if mutatedRow >= 0 and mutatedRow < len(grid) and grid[mutatedRow][col].isnumeric() and int(grid[mutatedRow][col])-item == 1:
            navigate(mutatedRow, col, listOfNines)
    for mutatedCol in horizontal:
        if mutatedCol >= 0 and mutatedCol < len(grid[0]) and grid[row][mutatedCol].isnumeric() and int(grid[row][mutatedCol])-item == 1:
            navigate(row, mutatedCol,listOfNines)
    return len(listOfNines)

for rowIndex, row in enumerate(grid):
    for columnIndex, col in enumerate(row):
        if col == '0':
           score+= navigate(rowIndex, columnIndex, set())

print("Part 1: ", score)