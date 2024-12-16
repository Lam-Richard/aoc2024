class Verifier():
    def __init__(self, args, total):
        self.args = args
        self.total = total
        self.length = len(args)
    
    def verify(self):
        curr = self.args[0]
        
        if (self.backtrack(curr, 1)):
            return self.total
        
        return 0

    def backtrack(self, curr, index):
        if index == self.length:
            return curr == self.total
        
        return self.backtrack(curr + self.args[index], index + 1) or self.backtrack(curr * self.args[index], index + 1)
            

with open("7/7.txt", "r") as f:
    lines = list(map(lambda line: line.strip(), f.readlines()))
    
    totals = list(map(lambda line : int(line[:line.index(":")]), lines))
    args = list(map(lambda line : [int(i) for i in line[line.index(":") + 2:].split(" ")], lines))
    
    res = 0
    
    for i in range(len(totals)):
        res += Verifier(args[i], totals[i]).verify()
        
    print(res)