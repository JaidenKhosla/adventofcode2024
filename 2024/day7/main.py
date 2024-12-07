import functools
import random

def validateWeight(line: str) -> int:
    # print(line)
    weight, nums = line.split(": ")
    nums = list(map(int,nums.split(" ")))
    weight = int(weight)
    
    for i in range(2**len(nums)):
        binary = list(bin(i)[2:].zfill(len(nums)-1)[::-1]+"_")
        tempNums = nums.copy()
        # print("".join(binary))
        newList = []
        breakPlease = False
        for temp, tempOperation in zip(tempNums, binary):
            # print("".join(newList))
            newList.append(str(temp))

            if len(newList) == 3:
                x1,y1,z1 = [str(newList.pop(0)) for _ in range(3)]

                newList.append(str(eval(x1+y1+z1)))
            newList.append("+" if tempOperation == "0" else "*" if tempOperation == "1" else "")
            if int(newList[0]) > weight:
                # print(newList[0],"too big!")
                breakPlease = True
                break
        
        if breakPlease: continue
        # print("".join(newList))
        num = int(newList[0])
        # print(num)

        if num == weight:
            # print(num,"\n")
            return num

        # print()

    return 0




with open("2024/day7/test.txt") as file:
    count = 0
    lines = file.read().strip().split("\n")

    for line in lines:
        count+=validateWeight(line)

    print("Part One ", count)

    file.close()