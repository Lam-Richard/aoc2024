with open("1/1.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda line : line.strip().split("   "), lines))
    firstList = list(map(lambda x : int(x[0]), lines))
    secondList = list(map(lambda x : int(x[1]), lines))
    print(sum([secondList.count(a) * a for a in firstList]))