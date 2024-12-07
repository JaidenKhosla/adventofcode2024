import copy
import tqdm

def partOne(strMap: list[list[str]]) -> tuple[int]:
    strMap = copy.deepcopy(strMap)
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    di = 0

    rows = len(strMap)
    columns = len(strMap[0])

    y,x = 0,0

    for i in range(rows):
        for j in range(columns):
            if strMap[i][j] == "^":
                y,x = i,j

    seen = set()

    while True:

        seen.add((y,x))

        nextY = y+directions[di][0]
        nextX = x+directions[di][1]

        if (nextY < 0 or nextY >= rows) or (nextX < 0 or nextX >= columns):
            break

        if strMap[nextY][nextX] == "#":
            di = (di+1)%4
            continue

        y,x = nextY,nextX
        strMap[y][x] = "0"
    return seen


def partTwo(strMap: list[list[str]]):

    x,y = 0,0

    for i in range(len(strMap)):
        for j in range(len(strMap)):
            if strMap[i][j] == "^":
                x,y = j,i
  
    def isALoop(ro,col) -> bool:
        if strMap[ro][col] in ("#","^"):
            return False
        

        strMap[ro][col] = "#"

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        rows, cols = len(strMap), len(strMap)

        loopSeen = set()

        loopDi = 0

        agentY, agentX = y,x

        while True:
            if (agentY, agentX, loopDi) in loopSeen:
                strMap[ro][col] = "."
                return True
            
            loopSeen.add((agentY,agentX, loopDi))

            nextY2 = agentY+directions[loopDi][0]
            nextX2 = agentX+directions[loopDi][1]

            if not (0 <= nextY2 < rows and 0 <= nextX2 < rows):
                strMap[ro][col] = "."
                return False
            
            if strMap[nextY2][nextX2] == "#":
                loopDi = (loopDi+1)%4
            else:
                agentY, agentX = nextY2, nextX2
    
    count = 0
    seen = partOne(strMap)
    for xx in tqdm.tqdm(seen):
        i,j = xx
        count+=isALoop(i,j)
    
    return count

with open("2024/day6/text.txt") as file:
    strMap = [list(i) for i in file.read().strip().split("\n")]

    print("Part One: ", len(partOne(strMap)))
    print("Part Two: ", partTwo(strMap))