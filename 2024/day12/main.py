import math,copy,time
with open("2024/day12/test.txt") as file:
    grid = [i.strip("\n") for i in file.readlines()]
    file.close()

count = 0
alreadyLooked = []

def look(y: int, x:int, perimeter=0, area=0, character=None):
    if not character:
        character = grid[y][x]
    elif y<0 or y>=len(grid) or x<0 or x>=len(grid[0]):
        return (1,0)
    elif (y,x) in alreadyLooked:
        return (0,0)
    elif character!=grid[y][x]:
        return (1,0)
    
    alreadyLooked.append((y,x))

    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (i,j) == (y,x):
                continue
            
            newPerimeter, newArea = look(i,j, 0, 1,character)
            perimeter+=newPerimeter
            area+=newArea
            print(perimeter,area)
            
    return (perimeter,area)


for y in range(len(grid)):
    for x in range(len(grid[0])):
        m,n = look(y,x,0,0)
        count+=m*n
print(count)

    
