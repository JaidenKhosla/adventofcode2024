def getWrappingPaper(x: str):
    l,w,h= list(map(int,x.split("x")))
    smallestSideArea = min(l*w, h*w, h*l)
    surfaceArea = 2*l*w + 2*w*h + 2*h*l
    return smallestSideArea+surfaceArea

def getRibbonLength(x: str):
    dimensions = sorted(list(map(int,x.split("x"))))
    s,m,l = dimensions
    length = s*2+m*2 + s*m*l
    return length


with open("2015/day2/text.txt") as file:
    num = 0
    num2 = 0
    for line in file.readlines():
        num+=getWrappingPaper(line)
        num2 += getRibbonLength(line)
    print(f"Part 1: {num}")
    print(f"Part 2: {num2}")
    file.close()