class Grid:
    def __init__(self, map:str):
        self.map: list[list[str]] = [list(i) for i in map.split("\n")]
        self.agentPos = self.findAgent()
        self.direction = self.getDirection()

    def findAgent(self) -> tuple[int]:
        for rowIndex,row in enumerate(self.map):
            for columnIndex,column in enumerate(row):
                if column in "<>v^":
                    return (rowIndex,columnIndex)
    def getDirection(self) -> tuple[int]:
        y,x = self.agentPos
        agent = self.map[y][x]
        if agent == "<":
            return (0,-1)
        elif agent == ">":
            return (0,1)
        elif agent == "^":
            return (-1,0)
        elif agent == "v":
            return (1,0)
        return (0,0)
    
    def addVectors(self, a: tuple[int], b: tuple[int]) -> tuple[int]:
        y1,x1 = a
        y2, x2 = b
        return (y1+y2, x1+x2)

    def changeDirectionBasedOnCollisions(self) -> int:
        while True:
            y,x = self.addVectors(self.agentPos,self.direction)
            if (y < 0 or y > len(self.map)-1) or (x < 0 or x > len(self.map[0])-1):
                return 0
            item = self.map[y][x]
            if item == "#":
                rY, rX = self.direction
                self.direction = (rX, -rY)
            else:
                break
        return 1
    
    def agentSee(self) -> list[tuple[int]]:
        return [(0,0)]

    def traverse(self) -> int:
        y,x = self.agentPos
        character = self.map[y][x]
        count = 0

        while(y < len(self.map) and x < len(self.map[0])):
            y,x = self.agentPos
            contniueMoving = self.changeDirectionBasedOnCollisions()
            if contniueMoving == 0:
                break

            nY, nX = self.addVectors(self.agentPos, self.direction)
            nItem = self.map[nY][nX]
            self.map[y][x] = "X" 
            self.map[nY][nX] = "X"
            self.agentPos = (nY,nX)

            # print("\n".join([" ".join(i) for i in self.map]))
            # print()

        return sum([i.count("X") for i in self.map])
    

with open("2024/day6/text.txt") as file:
    mapGrid = file.read()

    grid = Grid(mapGrid)

    print(f"Part One: {grid.traverse()}")

    file.close()