def oldVerifyLine(line):
    if isDuplicatesExist(line):
        return False

    if line != sorted(line) and line != sorted(line)[::-1]:
        return False
    
    absDiff = [abs(line[i] - line[i - 1]) for i in range(1, len(line))]
    return min(absDiff) >= 1 and max(absDiff) < 4

def isDuplicatesExist(line):
    return countDuplicates(line) != 0

def countDuplicates(line):
    return len(line) - len(set(line))

def isDuplicatesSalvageable(line):
    return countDuplicates(line) <= 1

def tryWithSingleDuplicate(line):
    duplicate = list(filter(lambda e : line.count(e) > 1, line))
    indices = list(filter(lambda i : line[i] == duplicate, range(len(line))))
    status = False
    for index in indices:
        newLine = line[:]
        newLine.pop(index)
        status = status or oldVerifyLine(newLine)
    return status

def countTurningPoints(line):
    isPeak = lambda i : line[i - 1] < line[i] and line[i + 1] < line[i]
    isValley = lambda i : line[i - 1] > line[i] and line[i + 1] > line[i]
    isTurningPoint = lambda i : isPeak(i) or isValley(i)
    candidates = range(2, len(line) - 1)
    return len(list(filter(isTurningPoint, candidates)))

def isTurningPointsSalvageable(line):
    return countTurningPoints(line) <= 1

def isTurningPointsExist(line):
    return countTurningPoints(line) == 0

def tryWithSingleTurningPoint(line):
    isPeak = lambda i : line[i - 1] < line[i] and line[i + 1] < line[i]
    isValley = lambda i : line[i - 1] > line[i] and line[i + 1] > line[i]
    isTurningPoint = lambda i : isPeak(i) or isValley(i)
    
    indices = list(filter(isTurningPoint, list(range(2, len(line) - 1))))
    indices.append(0)
    indices.append(-1)
    
    status = False
    for index in indices:
        newLine = line[:]
        newLine.pop(index)
        status = status or oldVerifyLine(newLine)
    return status

def isDrasticDrop(line):
    absDiff = [abs(line[i] - line[i - 1]) for i in range(1, len(line))]
    return not (min(absDiff) >= 1 and max(absDiff) < 4)

def countDrasticDrop(line):
    absDiff = [abs(line[i] - line[i - 1]) for i in range(1, len(line))]
    return len(list(filter(lambda e : e >= 4, absDiff)))

def isDrasticDropSalvageable(line):
    return countDrasticDrop(line) <= 1

def tryWithSingleDrasticDrop(line):
    absDiff = [abs(line[i] - line[i - 1]) for i in range(1, len(line))]
    return True

def verifyLine(line):
    if not isDuplicatesSalvageable(line):
        return False
    
    if isDuplicatesExist(line):
        return tryWithSingleDuplicate(line)
    
    if not isTurningPointsSalvageable(line):
        return False
    
    if isTurningPointsExist(line):
        return tryWithSingleTurningPoint(line)
    
    if not isDrasticDropSalvageable(line):
        return False
    
    if isDrasticDrop(line):
        return tryWithSingleDrasticDrop(line)
    
    return True

def bruteForce(line):
    for i in range(len(line)):
        newLine = line[:]
        newLine.pop(i)
        if oldVerifyLine(newLine):
            return True
    return False
        
with open("2/2.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda line : [int(a) for a in line.strip().split(" ")], lines))
    filteredLines = list(filter(bruteForce, lines))
    print(len(filteredLines))
    