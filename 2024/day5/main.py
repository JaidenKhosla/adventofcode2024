class Queue:
    def __init__(self):
        self.rules: dict[int,list[int]] = {}
    
    def validateRule(self, instruction: str):
        #47 | 53
        x,y = map(int, instruction.split("|"))

        self.rules[y] = self.rules.get(y,[])+[x]

    def validateInstruction(self, instruction:str) -> int:
        nums = list(map(int, instruction.split(",")))

        for index,num in enumerate(nums):
            beforeNumbers = filter(lambda x: x in nums, self.rules.get(num,[]))
            for beforeNumber in beforeNumbers:
                if beforeNumber not in nums[:index]:
                    return 0

        return nums[len(nums)//2]
    
    def check(self,queueList: list[int], nums: list[int],num: int):
        beforeNums = list(filter(lambda x: x in nums, self.rules.get(num,[])))
        if beforeNums:
             for beforeNum in beforeNums:
                if beforeNum not in queueList:
                    # print(f"{num} can't go before{list(beforeNums)}")
                    return False
        return True

    def fixInstruction(self, instruction: str) -> int:
        if self.validateInstruction(instruction) > 0:
            return 0
        
        queueList = []
        needToBeResolved = []
        nums = list(map(int, instruction.split(",")))

        while len(nums) > 0 or len(needToBeResolved) > 0:
            if len(needToBeResolved) > 0: 
                if self.check(queueList,nums+needToBeResolved, needToBeResolved[0]):
                    queueList.append(needToBeResolved.pop(0))
                else:
                    needToBeResolved.append(needToBeResolved.pop(0))
            if  len(nums) > 0:
                if self.check(queueList, nums+needToBeResolved, nums[0]):
                    queueList.append(nums.pop(0))
                else:
                    needToBeResolved.append(nums.pop(0))


        return queueList[len(queueList)//2]

with open("2024/day5/test.txt") as file:

    queue = Queue()

    lines = file.read().split("\n")

    partOne = 0
    partTwo = 0

    for line in lines:
        if "," in line:
            partOne += queue.validateInstruction(line)
            partTwo += queue.fixInstruction(line)
        elif "|" in line:
            queue.validateRule(line)
    print(f"Part One: {partOne}")
    print(f"Part Two: {partTwo}")
    file.close()