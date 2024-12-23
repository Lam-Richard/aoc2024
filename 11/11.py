class RuleApplier():
    def __init__(self):
        self.curr = None
        
        with open("11/11.txt", "r") as f:
            line = list(map(lambda line : line.strip(), f.readlines()))[0]
            self.curr = [int(i) for i in line.split()]            
    
    def check(self, n):
        if n == 0:
            return [1]
        
        str_n = str(n)
        len_str_n = len(str_n)
        
        if len_str_n % 2 == 0:
            return [int(str_n[:len_str_n // 2]), int(str_n[len_str_n // 2:])]
        
        return [2024 * n]
    
    def solve(self):
        i = 0
        while i != 75:
            new_list = []
            
            for num in self.curr:
                new_list += self.check(num)
                
            self.curr = new_list
            i += 1

            
    def print(self):
        print(len(self.curr))
        

ruleApplier = RuleApplier()
ruleApplier.solve()
ruleApplier.print()