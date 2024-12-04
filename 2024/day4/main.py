def usedInXMAS(strMap: list[str]) -> int:
    count = 0
    rows = ""
    cols = ["" for i in strMap[0]]
    diags = {}
    reversedDiags = {}
    #For horizontal and vertical search
    for rowIndex, row in enumerate(strMap):
        count+=row.count("XMAS") + row.count("SAMX")
        rows += row + " "
        for columnIndex, col in enumerate(row):
            cols[columnIndex]+=col
            originX = columnIndex
            originY = rowIndex

            while (originX > 0 and originX < len(row)) and (originY > 0 and originY < len(strMap)):
                originX-=1
                originY-=1
            
            reversedOriginX = columnIndex
            reversedOriginY = rowIndex

            while (reversedOriginX > 0 and reversedOriginX < len(row)) and (reversedOriginY > 0 and reversedOriginY < len(strMap)):
                reversedOriginX+=1
                reversedOriginY-=1

            diags[(originX,originY)] = diags.get((originX,originY),"")+strMap[rowIndex][columnIndex]
            reversedDiags[(reversedOriginX,reversedOriginY)] = reversedDiags.get((reversedOriginX, reversedOriginY),"")+strMap[rowIndex][columnIndex]

    for (p,r) in zip(diags.values(), reversedDiags.values()):
        count+=p.count("XMAS") + p.count("SAMX") + r.count("XMAS") + r.count("SAMX")
    cols = " ".join(cols)
    count+= cols.count("XMAS") + cols.count("SAMX")

    print(cols)
    print(rows)
    print(diags)
    print(reversedDiags)

    return count
with open("2024/day4/text.txt") as file:
    splittedFile = file.read().split("\n")
    partOne = usedInXMAS(splittedFile)
    print(partOne)