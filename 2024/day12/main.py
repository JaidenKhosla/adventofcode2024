import math,copy,time
with open("2024/day12/test.txt") as file:
    grid = [i.strip("\n") for i in file.readlines()]
    file.close()

regions = {}
#min row , max row, min col, max col, area, perimeter

for rowIndex, row in enumerate(grid):
    for columnIndex, item in enumerate(row):
        coords = (rowIndex,columnIndex)
        if regions.get(item):
            breakpls = False
            for group in regions[item]:
                for coord in group:
                    ma = [(o,l) for l in range(max(coords[1]-1, 0), min(coords[1]+2, len(grid[0]))) for o in range(max(coords[0]-1,0), min(coords[0]+2, len(grid))) if grid[o][l] == item]
                    gridCopy = [["." for i in range(len(grid[0]))] for j in range(len(grid))]
                    for u in ma:
                        y,x = u
                        gridCopy[y][x] = grid[y][x]
                    # print("\n".join(["".join(i) for i in gridCopy])+"\n")
                    # time.sleep(0.75)
                    if coord in ma:
                    # if abs(coord[0]-rowIndex) <= 1 and abs(coord[1]-columnIndex) <= 1:
                        # if item == "I": print(item, group, coord)
                        group.add(coords)
                        breakpls = True
                        break
            if not breakpls and len(list(filter(lambda x: coord in x, regions[item]))) == 0:
                regions[item].append(set())
                regions[item][-1].add(coords)
        else:
            regions[item] = [set()]
            regions[item][-1].add(coords)

totalCount = 0
alreadyDone = []
def getSubRegions(pos: set, letter: str):
    minRow = min(pos, key=lambda x: x[0])[0]
    minCol = min(pos, key=lambda x: x[1])[1]
    maxRow = max(pos, key=lambda x: x[0])[0]
    maxCol = max(pos, key=lambda x: x[1])[1]
    res=0
    for y in range(minRow,maxRow+1):
        for x in range(minCol, maxCol+1):
            character = grid[x][y]
            if character != letter:
                position = (y,x)
                for group in regions[character]:
                    if position in group:
                        x = group
                        groupRows = [min(group, key=lambda x: x[0])[0], max(group, key=lambda x: x[0])[0]]
                        groupCols = [min(group, key=lambda x: x[1])[1], max(group, key=lambda x: x[1])[1]]
                        if group not in alreadyDone and (groupRows[0] > minRow and groupRows[1] < maxRow) and (groupCols[0] > minCol and groupCols[1] < maxCol): 
                            alreadyDone.append(group)
                            res+=getSubRegions(x,character)

    total = res
    for point in pos:
        



for region in regions:
    for group in regions[region]:
        gridCopy = [["." for i in range(len(grid[0]))] for j in range(len(grid))]
        for coord in group:
            y,x = coord
            gridCopy[y][x] = region

        print("\n".join(["".join(i) for i in gridCopy])+"\n")
        time.sleep(0.75)
        area = len(group)
        perimeter = getSubRegions(group,region)
        print(region,perimeter,area, perimeter*area)

        totalCount += perimeter*area
print(totalCount)
