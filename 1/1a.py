with open("1/1.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda line : line.strip().split("   "), lines))
    firstList = list(map(lambda x : int(x[0]), lines))
    secondList = list(map(lambda x : int(x[1]), lines))
    firstList.sort()
    secondList.sort()
    distances = list(map(lambda n : abs(firstList[n] - secondList[n]), range(1000)))
    print(sum(distances))

    