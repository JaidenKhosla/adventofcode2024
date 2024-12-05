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
    
    def fixInstruction(self, instruction: str) -> int:
        if self.validateInstruction(instruction) > 0:
            return 0
        
        queueList = []

        nums = list(map(int, instruction.split(",")))
        
        offset = 0

        while len(nums) > 0:
            num = nums[0+offset]

            canBePrinted = True

            beforeNums = filter(lambda x: x in nums, self.rules.get(num,[]))

            for beforeNum in beforeNums:
                if beforeNum not in queueList:
                    canBePrinted = False
                    break
            if not canBePrinted:
                nums.pop(0)
                nums.insert(1,num)
                continue
            offset = 0

            queueList.append(num)
            nums.pop(0+offset)
        print(queueList)
        return queueList[len(queueList)//2]

with open("2024/day5/test.txt") as file:

    queue = Queue()

    lines = file.read().split("\n")

    partOne = 0

    for line in lines:
        if "," in line:
            partOne += queue.validateInstruction(line)
            print(queue.fixInstruction(line))
        elif "|" in line:
            queue.validateRule(line)
    print(f"Part One: {partOne}")
    file.close()