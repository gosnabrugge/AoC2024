# -*- coding: utf-8 -*-
"""
Advent of Code day 5 script
"""
import math
import time
t0 = time.time()

#%%# read input file #%%#
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

rules = lines[0:1176]
updates = lines[1177:1389]

# collect rules in dictionary
rulesDict = dict()
for iRule in range(len(rules)):
    entrees = rules[iRule].split('|')
    key = entrees[0]
    Num = int(entrees[1])
    if not key == '.':
        if key in rulesDict: # add entree coordinates to dictionary
            rulesDict[key].append(Num)
        else: # create new entree in dictionary
            rulesDict[key] = [Num]

# convert updates to integer list    
for i in range(len(updates)):
    updates[i] = list(map(int,updates[i].split(',')))


#%%# Part 1 #%%#
resultsPart1 = 0

incorrectUpdates = [] # collected for part 2
for update in updates:
    correctUpdate = True
    for i in range(len(update)):
        for j in range(i+1,len(update)):
            num1 = update[i]
            num2 = update[j]
            if num1 in rulesDict[str(num2)]:
                correctUpdate = False
                break
        if not correctUpdate:
           break 
              
    if correctUpdate: # only consider correct updates
        resultsPart1 += update[math.floor(len(update)/2)]
    else:
        incorrectUpdates.append(update)

#%%# Part 2 #%%#
resultsPart2 = 0

for update in incorrectUpdates:
    newUpdate = [update[0]]
    for i in range(1,len(update)):
        newInd = -1
        for j in range(len(newUpdate)):
            if newUpdate[j] in rulesDict[str(update[i])]: 
                newInd = j
                break

        if newInd == -1:
            newUpdate.append(update[i])
        else:
            newUpdate = newUpdate[0:newInd] + [update[i]] + newUpdate[newInd::]
    
    resultsPart2 += newUpdate[math.floor(len(newUpdate)/2)]
    
#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
