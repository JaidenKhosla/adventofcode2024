import tqdm
import itertools


def generateCombinations(operations: int, partOne):
    operators =  ["+","*"]if partOne else ["+","*","||"]
    x = list(itertools.product(operators, repeat=operations))
    return x

def executeExpression(nums, operations) -> int:
    nums = nums.copy()
    res = nums[0]
    for index, operation in enumerate(operations):
        if operation == "+":
            res+=nums[index+1]
        elif operation == "*":
            res*=nums[index+1]
        elif operation == "||":
            res = int(str(res)+str(nums[index+1]))
    return res

def validateWeight(line: str, tenaryOP=False) -> int:
    # print(line)
    weight, nums = line.split(": ")
    nums = list(map(int,nums.split(" ")))
    weight = int(weight)
    
    operations = generateCombinations(len(nums)-1, not tenaryOP)
    for operation in operations:
        result = executeExpression(nums, operation)
        if result == weight:
            # print(result, tenaryOP, operation)
            return weight
    
    return 0




with open("2024/day7/test.txt") as file:
    count = 0
    count2 = 0
    lines = file.read().strip().split("\n")

    for line in tqdm.tqdm(lines):
        count+=validateWeight(line)
        count2+=validateWeight(line,True)
    print("Part One: ", count)
    print("Part Two: ", count2)

    file.close()