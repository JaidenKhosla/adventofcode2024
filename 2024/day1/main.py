import functools

left = []
right = []

def getDistance(x: str) -> int:
    x = x.replace("\n","")
    nums = list(map(int,filter(lambda s: s.isnumeric() ,x.split(" "))))
    leftNum = nums[0]
    rightNum = nums[-1]
    left.append(leftNum)
    right.append(rightNum)


with open("2024/day1/text.txt") as file:
    x1 = 0
    x2 = 0
    for line in file.readlines():
        getDistance(line)
  
    left.sort()
    right.sort()


    #part 1
    for a,b in zip(left, right):
        x1 += abs(a-b)
  #part 2
    for num in left:
         x2+= (num*right.count(num))
    
    print(f"PART ONE: {x1}\nPART TWO: {x2}")
    file.close()
