
x1 = 0
x2 = 0

def validate(x: str) -> int:

    prevIncreasing = False
    isIncreasing = False

    x = x.replace("\n", "")

    nums = list(map(int,x.split(" ")))

    for i in range(0, len(nums)-1):
        num1 = nums[i]
        num2  = nums[i+1]

        distance = num2 - num1

        if distance > 0:
            isIncreasing = True
        else:
            isIncreasing = False

        if not (distance >= -3 and distance <= 3) or distance == 0 or (i != 0 and prevIncreasing != isIncreasing):
            return 0
        
        prevIncreasing = isIncreasing

    return 1

def validate2(x: str) -> int:

    fixable = True

    diff = 0

    prevIncreasing = False
    isIncreasing = False

    x = x.replace("\n", "")

    nums = list(map(int,x.split(" ")))

    for i in range(0, len(nums)-1):
        num1 = nums[i]
        num2  = nums[i+1]

        distance = num2 - num1

        if distance > 0:
            isIncreasing = True
        else:
            isIncreasing = False

        if not (distance >= -3 and distance <= 3) or distance == 0 or (i != 0 and prevIncreasing != isIncreasing):
            if fixable:
                fixable = False
            else:
                return 0
        
        prevIncreasing = isIncreasing
    return 1

with open("day2/text.txt") as file:
    for line in file.readlines():
        #PART ONE
        x1+=validate(line)
        x2+=validate2(line)
        print(f"{line.replace("\n","")}: {"SAFE" if validate2(line) == 1 else "UNSAFE"}")
    print(f"Part 1: {x1}\nPart 2: {x2}")