import tqdm, re
def generateLink(line: str, partTwo = False) -> list:
    x = []
    count = 0

    positions = {}

    for index, character in enumerate(line):
        if index%2==0:
            if not partTwo:
                for _ in range(int(character)):
                    positions.setdefault(str(count), list())
                    positions[str(count)].append(len(x))
                    x.append(str(count))
            else:
                x.append([count for i in range(int(character))])
            count+=1
        else:
            if partTwo:
                x.append(["." for i in range(int(character))])
            else:
                for i in range(int(character)):
                    x.append(".")
    return [x,positions]

def partOne(line: str):
    count = 0
    iterationCount = 0
    line: list = generateLink(line)[0]
    newNums = [i for i in range(len(line)) if line[i].isnumeric()]
    periodList = ["." for i in range(line.count("."))]
    for index in tqdm.tqdm(range(len(line))):
        if line[index] == ".":
           newNum = newNums.pop()
           if index > newNum: break
           line[index] = line[newNum]
           line.pop(newNum)
           line.append(".")
        item = line[index]
        count+= int(item)*index
    return count



def partTwo(line: str):
    size = [0]*len(line)
    loc = [0]*len(line)

    def make_fileSys(line: str):
        blocks = []
        is_file = True
        id = 0
        for i in line:
            x = int(i)
            if is_file:
                loc[id] = len(blocks)
                size[id] = x
                blocks += [id]*x
                id +=1
                is_file = False
            else:
                blocks+=[None]* x
                is_file = True
        return blocks
    
    filesys = make_fileSys(line)

    def move(arr):
        big = 0
        while size[big] > 0:
            big+=1
        big -=1

        for move in tqdm.tqdm(range(big,-1,-1)):
            free_space = 0
            first_free =0

            while first_free < loc[move] and free_space < size[move]:
                first_free += free_space
                free_space = 0
                while arr[first_free] != None:
                    first_free +=1
                while first_free + free_space < len(arr) and arr[first_free+free_space] == None:
                    free_space += 1
            
            if first_free >= loc[move]:
                continue
            

            for idx in range(first_free, first_free+size[move]):
                arr[idx] = move
            for idx in range(loc[move], loc[move]+size[move]):
                arr[idx] = None
            
        return arr
    
    def checkSum(arr):
        ans = 0
        for index, i in enumerate(arr):
            if i != None:
                ans += i*index
        return ans
    
    return checkSum(move(filesys))
with open("2024/day9/test.txt") as file:

    line = file.read().strip().replace("\n","")

    print("Part One: ",partOne(line))
    print("Part Two: ", partTwo(line))
    file.close()