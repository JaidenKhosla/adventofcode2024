import re

class lightGrid:
    def __init__(self, width: int, height: int, brightness=False) -> None:
        self.width = width
        self.height = height
        self.brightness = brightness
        if not brightness:
            self.grid: list[list[bool]] = [[False for i in range(self.width)] for j in range(self.height)]
        else:
            self.grid: list[list[int]] = [[0 for i in range(self.width)] for j in range(self.height)]

    def getAllLitLights(self) -> int:
        count = 0
        for row in self.grid:
            for col in row:
                if not self.brightness:
                    if col: count+=1
                else:
                    count += col
        return count

    def toggle(self,x: int, y: int):
        if self.brightness:
            self.grid[y][x]+=2
        else:
            self.grid[y][x] = not self.grid[y][x]

    def turnOff(self, x: int, y: int):
        if self.brightness:
            self.grid[y][x] = max(0,self.grid[y][x]-1)
        else:
            self.grid[y][x] = False
    
    def turnOn(self, x: int, y: int):
        if self.brightness:
            self.grid[y][x]+=1
        else:
            self.grid[y][x] = True
    
    def getRange(self,x1: int, y1: int, x2: int, y2: int) -> list[tuple]:
        x = []

        highestRow, lowestRow = sorted([y1,y2])
        lowestColumn, highestColumn = sorted([x1,x2])
        for row in range(highestRow, lowestRow+1):
            for column in range(lowestColumn, highestColumn+1):
                x.append((row,column))
        
        return x
    

    def executeCommand(self, cmd: str):

        coordPattern = re.compile(r"(\d+),(\d+) through (\d+),(\d+)")

        actualCmd = self.turnOn if "turn on" in cmd else self.turnOff if "turn off" in cmd else self.toggle

        x1,y1,x2,y2 = list(map(int,coordPattern.findall(cmd)[0]))

        lights = self.getRange(x1,y1,x2,y2)

        for light in lights:
            actualCmd(*light)

grid1 = lightGrid(1000,1000)
grid2 = lightGrid(1000,1000, True)
with open("2015/day6/text.txt") as file:
    for line in file.readlines():
        grid1.executeCommand(line)
        grid2.executeCommand(line)
    partONE = grid1.getAllLitLights()
    partTWO = grid2.getAllLitLights()
    print(f"Part One: {partONE}")
    print(f"Part Two: {partTWO}")
    file.close()