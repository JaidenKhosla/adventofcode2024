
x1 = 0
x2 = 0

def validate(a: int,b: int, prevIncreasing: bool, i: int) -> bool:
    
    if a==b: return False
    
    distance = b-a

    if distance > 0:
            isIncreasing = True
    else:
        isIncreasing = False

    if abs(distance) > 3 or (i != 0 and prevIncreasing != isIncreasing):
        return False
    return True

def partOne(x: str) -> int:
    prevIncreasing = False

    x = x.replace("\n", "")

    nums = list(map(int,x.split(" ")))

    for i in range(0, len(nums)-1):
        num1 = nums[i]
        num2  = nums[i+1]

        if not validate(num1,num2,prevIncreasing,i):
            return 0
        
        prevIncreasing = (num2 - num1) > 0

    return 1

def partTwo(x: str) -> int:


    if partOne(x) == 1:
        return 1

    x = x.replace("\n", "")
        
    nums = list(map(int,x.split(" ")))

    for i in range(len(nums)):
                        
        newList = nums[:i] + nums[i+1:]

        if partOne(" ".join(list(map(str,newList)))) == 1:
            return 1
    return 0
        

with open("day2/text.txt") as file:
    numOfCorrect1 = 0
    numOfCorrect2 = 0

    lines = file.readlines()

    numOfLines = len(lines)

    for line in lines:
        #PART ONE

        validation1 = partOne(line)
        validation2 = partTwo(line)

        x1+=validation1
        x2+=validation2

        numOfCorrect1+=validation1
        numOfCorrect2+=validation2

        if validation2 == 0:
            print(line)
    print(f"Part 1: {x1}\nPart 2: {x2}")
    print(f"NUMBER OF WRONG FOR PT 1: {numOfLines-numOfCorrect1}\nNUMBER OF WRONG FOR PT 2: {numOfLines-numOfCorrect2}")
    file.close()