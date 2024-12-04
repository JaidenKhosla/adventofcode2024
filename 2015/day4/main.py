import hashlib

input_string = "bgvyzdsv"

finalHash = ""
finalHash2 = ""

count = 0
count2 = 0

def digest(input: str, count: int):
    encoded = (input_string+str(count)).encode()
    _finalHash = hashlib.md5(encoded).hexdigest()
    return _finalHash

while not finalHash2.startswith("0"*6):
    if not finalHash.startswith("0"*5):
        count+=1
        finalHash = digest(input_string, count)

    if not finalHash2.startswith("0"*6):
        count2+=1
        finalHash2 = digest(input_string, count2)

print("PART ONE:")
print(f"HASH: {finalHash}\nCOUNT: {str(count)}")
print("PART TWO:")
print(f"HASH: {finalHash2}\nCOUNT: {str(count2)}")