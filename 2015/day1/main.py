def getPos(x: str) -> int:
    pos = 0
    for iteration, character in enumerate(x):
        pos+=(1 if character == "(" else -1)
        if pos < 0: return iteration+1

with open("2015/day1/text.txt") as file:
    text = file.read()
    n = text.count("(") + text.count(")") * -1
    print(f"PART ONE: {n}")
    print(f"PART TWO: {getPos(text)}")
    file.close()