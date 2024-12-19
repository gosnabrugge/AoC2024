# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day .. script
author: g.osnabrugge
"""
#import numpy as np
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile):
    patterns = []
    for i,line in enumerate(open(inputFile)):
        if i == 0: 
            towels = line.split(', ')
            towels[-1] = towels[-1].rstrip()
        elif i > 1: patterns.append(line.rstrip())
        
    return towels, patterns
#%%# readout puzzle input file #%%#
towels, patterns = loadData('input.txt')
# inputFile = 'input.txt'

# # extract all contents of input file
# inputs = open(inputFile).read()

# # extract entrees per puzzle line
# for line in open(inputFile):
#     entrees = list(map(int,line.split(' ')))

# # readout puzzle txt file into separate string lines (without white spaces)
# with open(inputFile) as file:
#     lines = [line.rstrip() for line in file]

#%%%# Part 1 #%%#
resultsPart1 = 0

# determine longest towel pattern
L = 0
for towel in towels:
    if len(towel) > L: L = len(towel)

# find set of towels matching the pattern
for pattern in patterns:
    l = L
    while len(pattern)>0:
        if l > len(pattern): l = len(pattern)
        subPattern = pattern[0:l]
        
        if subPattern in towels:
            pattern = pattern[l::] # remove matched segment
            l = L
        else: l -= 1
        
        if l == 0: break
    
    if len(pattern) == 0: resultsPart1 += 1



#%%%# Part 2 #%%#
resultsPart2 = 0

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
