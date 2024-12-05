import re

pattern = r'mul\(([1-9]\d{0,2}|0),([1-9]\d{0,2}|0)\)|(do\(\))|(don\'t\(\))'

def find_mul_groups(text):
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        print(match)
        if match[0] and match[1]:  # mul(X,Y)
            result.append(int(match[0]) * int(match[1]))
        elif match[2]:  # do()
            result.append(True)
        elif match[3]:  # don't()
            result.append(False)
    
    shouldAdd = True
    res = 0
    
    for operation in result:
        if type(operation) == bool:
            shouldAdd = operation
        elif shouldAdd:
            res += operation
        else:
            print(f"Not adding {operation} because shouldAdd was False")
    
    return res
    


with open("3/3.txt", "r") as f:
    lines = f.readlines()
    line = "".join(lines) 
    print(find_mul_groups(line))

