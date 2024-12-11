import tqdm

cache = {}
def solve(x: int, iteration: int) -> int:
    if iteration == 0:
        return 1
    if (x,iteration) in cache:
        return cache[(x,iteration)]
    if x == 0:
        result = solve(1, iteration-1)
    elif len(str(x))%2==0:
        y = str(x)
        half = len(y)//2
        result = solve(int(y[:half]), iteration-1) + solve(int(y[half:]), iteration-1)
    else:
        result = solve(x*2024, iteration-1)
    
    cache[(x,iteration)] = result
    return result


with open("2024/day11/text.txt") as file:
    nums = list(map(int, file.read().strip("\n").split(" ")))
    res = 0

    for num in tqdm.tqdm(nums):
        res+=solve(num,25)
    
    print("PART ONE: ",res)
    cache = {}
    res = 0
    for num in tqdm.tqdm(nums):
        res+=solve(num,75)
    print("PART TWO: ", res)