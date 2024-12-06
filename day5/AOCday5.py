# -*- coding: utf-8 -*-
"""
Advent of Code day 5 script
"""
import math

#### helper functions ####


#### read input file ####
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

# extract rules from input
rules = lines[0:1176]
for i in range(len(rules)):
    rules[i] = list(map(int,rules[i].split('|')))

# extract updates from input    
updates = lines[1177:1389]
for i in range(len(updates)):
    updates[i] = list(map(int,updates[i].split(',')))


#### Part 1 ####
resultsPart1 = 0


# find all correct updates
incorrectUpdates = []
for update in updates:
    correctUpdate = True
    for rule in rules:
        indices1 = [i for i,val in enumerate(update) if val==rule[0]]
        indices2 = [i for i,val in enumerate(update) if val==rule[1]]
        if len(indices1) >= 1 and len(indices2) >= 1:
            if max(indices1) > min(indices2):
                correctUpdate = False
                incorrectUpdates.append(update)
                break
            
    if correctUpdate: # only consider correct updates
        resultsPart1 += update[math.floor(len(update)/2)]
        
    
print('Part 1: '+ str(resultsPart1))

#### Part 2 ####
resultsPart2 = 0

for update in incorrectUpdates:
    newUpdate = []
    for num in update:
        indices = []
        for rule in rules:
            indices += [i for i,val in enumerate(newUpdate) if num==rule[0] and val == rule[1]]
        
        if len(indices) == 0:
            newUpdate.append(num)
        else:
            indNum = min(indices)
            newUpdate = newUpdate[0:indNum] + [num] + newUpdate[indNum::]
    
    resultsPart2 += newUpdate[math.floor(len(newUpdate)/2)]
    
print('Part 2: '+ str(resultsPart2))

