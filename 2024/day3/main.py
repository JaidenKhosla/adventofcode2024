import re

def getMuls(x: str, includeDoDont = False) -> list[int]:

    products = []

    regexPattern = re.compile(r"mul\((\d+),(\d+)\)")
    
    doDontPattern = re.compile(r"(don't\(\))||(do\(\))")

    if not includeDoDont:
        allInstances = regexPattern.findall(x)

        for instance in allInstances:
            num1 = int(instance[0])
            num2 = int(instance[1])
            
            product: int = num1*num2

            products.append(product)
    else:
       indexes = [m for m in doDontPattern.finditer(x) if m.group()]
       for i in range(len(indexes)):
           curr = indexes[i]
           if i == 0:
               products+=getMuls(x[:curr.start()])
           nextIndex = indexes[i+1].start() if i+1 < len(indexes) else len(x)
           
           if curr.group() == "do()":
              haystack = x[curr.end():nextIndex]
              products+=getMuls(haystack)
    return products


with open("day3/text.txt") as file:
    
    text = file.read()

    sumOfNums = sum(getMuls(text))

    sumOfNumsForPT2 = sum(getMuls(text,True))
    print(f"ANSWER FOR PT 1: {sumOfNums}")
    print(f"ANSWER FOR PT 2: {sumOfNumsForPT2}")