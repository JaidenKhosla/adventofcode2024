
def addTwoVectors(a: tuple[int,int], b: tuple[int,int]) -> tuple[int,int]:
    return (a[0]+b[0], a[1]+b[1])
        


with open("2015/day3/text.txt") as file:
    directions = file.read()

    santaDirections = directions[0::2]
    roboSantaDirections = directions[1::2]

    key = {"^": (0,1), "v": (0,-1), ">": (1,0), "<": (-1,0)}    

    pos = (0,0)

    houses = {
        (0,0) : 1
    }

#PART ONE
    for direction in directions:
        pos = addTwoVectors(pos,key.get(direction,(0,0)))
        houses[pos] = houses.get(pos,0) + 1
    amtOfHouses = len(houses)
   
    santaPos = (0,0)
    roboSantaPos = (0,0)

    houses = {
        (0,0) : 1
    }

    for s,r in zip(santaDirections, roboSantaDirections):
        santaPos = addTwoVectors(santaPos,key.get(s,(0,0)))
        roboSantaPos = addTwoVectors(roboSantaPos,key.get(r,(0,0)))

        houses[santaPos] = houses.get(santaPos,0) + 1
        houses[roboSantaPos] = houses.get(roboSantaPos, 0) + 1

    amtOfHouses2 = len(houses)    

    
    print(f"NUMBER OF HOUSES VISITED: {amtOfHouses}")
    print(f"NUMBER OF HOUSES VISITED WITH ROBO SANTA: {amtOfHouses2}")
    
    file.close()