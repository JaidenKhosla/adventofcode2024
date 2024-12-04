numberOfNiceStrings = 0
numberOfNiceStrings2 = 0

def validate(x: str) -> bool:

    hasDupeLetter = False
    vowels = 0

    for i in ["ab","cd","pq","xy"]:
        if i in x: 
            return False
        
    for i in range(len(x)):
        character = x[i]
        if not hasDupeLetter and i < len(x)-1:
            nextCharacter = x[i+1]
            if character == nextCharacter:
                hasDupeLetter = True
        
        if character in "aeiou":
            vowels+=1

    return hasDupeLetter and vowels >= 3

def validate2(x: str) -> bool:

    hasPair = False
    pairsMap: dict[str, list[int]] = {}

    hasDoublePair = False

    for i in range(len(x)):
        if not hasPair and i <= len(x)-3:
            a = x[i]
            c = x[i+2]
            if a == c:
                hasPair = True
        if i < len(x)-1:
            currChar = x[i]
            nextChar = x[i+1]

            combo = currChar+nextChar

            pairsMap[combo] = pairsMap.get(combo,[]) + [i, i+1]
        
        for pair in pairsMap.values():
            if len(pair)/2 < 2:
                continue
            
            for index, item in enumerate(pair):
                if item in pair[:index]:
                    continue
            hasDoublePair = True

    return hasPair and hasDoublePair

with open("2015/day5/text.txt") as file:
    for line in file.readlines():
        if validate(line):
            numberOfNiceStrings+=1
        if validate2(line):
            numberOfNiceStrings2+=1
        else:
            print(line)
    print(f"NUMBER OF NICE STRINGS FOR PART ONE: {str(numberOfNiceStrings)}")
    print(f"NUMBER OF NICE STRINGS FOR PART TWO: {str(numberOfNiceStrings2)}")
    file.close()