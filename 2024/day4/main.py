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

            while (originX > 0 and originY > 0):
                originX-=1
                originY-=1
            
            reversedOriginX = columnIndex
            reversedOriginY = rowIndex

            while reversedOriginX < len(rows) -1 and reversedOriginY > 0:
                reversedOriginX+=1
                reversedOriginY-=1
            diags[(originX,originY)] = diags.get((originX,originY),"")+strMap[rowIndex][columnIndex]
            reversedDiags[(reversedOriginX, reversedOriginY)] = reversedDiags.get((reversedOriginX, reversedOriginY),"")+strMap[rowIndex][columnIndex]

    for (p,r) in zip(diags.values(), reversedDiags.values()):
        count+=p.count("XMAS") + p.count("SAMX") + r.count("XMAS") + r.count("SAMX")
    cols = " ".join(cols)
    count+= cols.count("XMAS") + cols.count("SAMX")

    return count

def usedInXofMAS(strMap: list[str]) -> int:

    count = 0

    for rowIndex, row in enumerate(strMap):
        for columnIndex, column in enumerate(row):
            character = column
            if character != "A" or rowIndex-1 < 0 or rowIndex+1 > len(strMap)-1 or columnIndex-1 < 0 or columnIndex+1 > len(row)-1:
                continue
            
            corners = "".join([strMap[rowIndex-1][columnIndex-1], strMap[rowIndex-1][columnIndex+1],strMap[rowIndex+1][columnIndex-1], strMap[rowIndex+1][columnIndex+1]])
            if corners in ["MSMS","SMSM","MMSS","SSMM"]:
                count+=1
    return count


with open("2024/day4/text.txt") as file:
    splittedFile = file.read().split("\n")
    partOne = usedInXMAS(splittedFile)
    print(f"PARTONE: {partOne}")
    partTwo = usedInXofMAS(splittedFile)
    print(f"PARTTWO: {partTwo}")

#spent two hours trying to figure out what was wrong with the my left diagonal for usedInXmas. Turns out it was a single boolean torturing me.