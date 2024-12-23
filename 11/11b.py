class RuleApplier():
    def __init__(self):
        self.res = 0
        self.line = None
        self.cache = {} # Key: (num, timeLeft) Value: Number of Stones
        
        with open("11/11.txt", "r") as f:
            self.line = list(map(lambda line : line.strip(), f.readlines()))[0]
            self.line = [int(i) for i in self.line.split()]      
            
    def check(self, n, time):
        if time == 0:
            return 1
        
        if (n, time) in self.cache:
            return self.cache[(n, time)]
        
        if n == 0:
            self.cache[(n, time)] = self.check(1, time - 1)
            return self.cache[(n, time)]
        
        str_n = str(n)
        len_str_n = len(str_n)
        
        if len_str_n % 2 == 0:
            first_part = int(str_n[:len_str_n // 2])
            second_part = int(str_n[len_str_n // 2:])
            self.cache[(n, time)] = self.check(first_part, time - 1) + self.check(second_part, time - 1)
            return self.cache[(n, time)]
        
        self.cache[(n, time)] = self.check(n * 2024, time - 1)
        return self.cache[(n, time)]
    
    def solve(self):
        self.res = sum(list(map(lambda num : self.check(num, 75), self.line)))
        return
            
    def print(self):
        print(self.res)

ruleApplier = RuleApplier()
ruleApplier.solve()
ruleApplier.print()