import copy

def partOne(grid):
    positions = set()

    antinodePositions = set()

    freq = {}
    count = 0

    for rowIndex, row in enumerate(grid):
        for columnIndex, column in enumerate(row):
            y1,x1 = rowIndex, columnIndex

            freq.setdefault(grid[y1][x1], set())

            if grid[y1][x1] != "." and grid[y1][x1] != "#":
                for pos in freq[grid[y1][x1]]:
                    y2, x2 = pos

                    dY1, dX1 = (y2-y1, x2-x1)
                    dY2, dX2 = (y1-y2, x1-x2)

                    y3,x3 = y2+dY1, x2+dX1
                    y4, x4 = y1+dY2, x1+dX2

                    if (y3 >= 0 and y3 < len(grid)) and (x3 >= 0 and x3 < len(grid[0])):
                        antinodePositions.add((y3,x3))
                    
                    if (y4 >= 0 and y4 < len(grid)) and (x4 >=0 and x4 < len(grid[0])):
                        antinodePositions.add((y4,x4))

                freq[grid[y1][x1]].add((y1,x1))
    return len(antinodePositions)

def partTwo(grid):
    positions = set()

    antinodePositions = set()

    freq = {}

    for rowIndex, row in enumerate(grid):
        for columnIndex, column in enumerate(row):
            y1,x1 = rowIndex, columnIndex

            freq.setdefault(grid[y1][x1], set())

            if grid[y1][x1] != "." and grid[y1][x1] != "#" and "".join(["".join(i) for i in grid]):
                antinodePositions.add((y1,x1))
                for pos in freq[grid[y1][x1]]:
                    y2, x2 = pos

                    dY1, dX1 = (y2-y1, x2-x1)
                    dY2, dX2 = (y1-y2, x1-x2)
                    y3,x3 = y2+dY1, x2+dX1
                    y4, x4 = y1+dY2, x1+dX2

                    while (y3 >= 0 and y3 < len(grid)) and (x3 >= 0 and x3 < len(grid[0])):
                        if grid[y3][x3] == ".":
                            grid[y3][x3] = "#"
                        antinodePositions.add((y3,x3))
                        y3+=dY1
                        x3+=dX1
                    
                    while (y4 >= 0 and y4 < len(grid)) and (x4 >=0 and x4 < len(grid[0])):
                        if grid[y4][x4] == ".":
                            grid[y4][x4] = "#"
                        antinodePositions.add((y4,x4))
                        y4+=dY2
                        x4+=dX2

                freq[grid[y1][x1]].add((y1,x1))
    # print("\n".join(["".join(i) for i in grid]))
    return len(antinodePositions)

with open("2024/day8/text.txt") as file:
    
    grid = [list(i.replace("\n","")) for i in file.readlines()]
    print("Part One: ",partOne(grid))
    print("Part Two: ", partTwo(grid))
    file.close()

