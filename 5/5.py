with open("5/5.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x : x.strip(), lines))
    separator = lines.index("")
    rules = lines[:separator]
    
    
    updates = [[int(e) for e in l.split(",")] for l in lines[separator + 1:]]
    
    prerequisites = {} 
    

    for rule in rules:
        separator = rule.index("|")
        condition = int(rule[:separator])
        course = int(rule[separator + 1:])
        
        prerequisites[course] = prerequisites.get(course, []) + [condition]
        
    def checkUpdate(update):
        checker = { update[i] : i for i in range(len(update)) }

        for j in range(len(update)):
            for condition in prerequisites.get(update[j], []):
                if checker.get(condition, None) and checker[condition] > j:
                    print(f"{update[j]} requires {condition} which is index {checker[condition]}")
                    return 0
        
        assert len(update) % 2 != 0
        return update[len(update) // 2]
      
    # print(prerequisites) 
    count = 0
    for update in updates:
        count += checkUpdate(update)
    print(count)
