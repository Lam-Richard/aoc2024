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
    
    def updateIsIncorrect(update):
        checker = { update[i] : i for i in range(len(update)) }

        for j in range(len(update)):
            for condition in prerequisites.get(update[j], []):
                if checker.get(condition, None) and checker[condition] > j:
                    return True
                
        return False
    
    def fixUpdate(update):
        preUpdate = update
        print(f"Broken Update: {update}")
        checker = { update[i] : i for i in range(len(update)) }

        j = 0
        while j != len(update):
            safe = True
            for condition in prerequisites.get(update[j], []):
                if checker.get(condition, None) and checker[condition] > j:
                    print(f"{update[j]} requires {condition} which is index {checker[condition]}")
                    safe = False
                    break
                    # [. . . J . . . Condition . . .]
                    # [. . . Condition J . . . . . .]
            if not safe:
                print(f"Prior Update: {update}")
                newUpdate = update[:j]
                newUpdate.append(condition)
                newUpdate.append(update[j])
                newUpdate += [e for e in update[j:] if (e != condition and e != update[j])]
                update = newUpdate
                print(f"Revised Update: {update}")
                checker = { update[i] : i for i in range(len(update)) }
            else:
                j += 1
        
        assert len(preUpdate) == len(update)
        return update[len(update) // 2]                
          
    incorrectUpdates = list(filter(updateIsIncorrect, updates))
    res = 0
    for update in incorrectUpdates:
        res += fixUpdate(update)
    print(res)