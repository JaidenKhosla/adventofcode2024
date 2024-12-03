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


with open("day1/text.txt") as file:
    x = 0
    for line in file.readlines():
        getDistance(line)
  
# for part one
#     left.sort()
#     right.sort()


  
#     for a,b in zip(left, right):
#         x += abs(a-b)
  #part 2
    for num in left:
         x+= (num*right.count(num))
    print(x)

