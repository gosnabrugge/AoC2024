# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 11 script
author: g.osnabrugge
"""
#import numpy as np
from collections import defaultdict
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile):
    stones = defaultdict(int)
    with open(inputFile) as file:
        for line in file:
            numbers = line.split(' ')
            for num in numbers:
                stones[int(num)] += 1
    return stones

def blink(stones):
    nextStones = defaultdict(int)
    for stone, occurrences in stones.items():
        nDigits = len(str(stone))
        if stone == 0: # rule 1
            nextStones[1] += occurrences
        elif nDigits%2 == 0: # rule 2
            lHalf = int(str(stone)[0:int(nDigits/2)])
            rHalf = int(str(stone)[int(nDigits/2)::])
            nextStones[lHalf] += occurrences
            nextStones[rHalf] += occurrences
        else: # rule 3
            nextStones[stone*2024] += occurrences
    
    return nextStones

#%%# readout puzzle input file #%%#
stones = loadData('input.txt')

#%%%# Part 1 & 2  #%%#
resultsPart1 = 0
resultsPart2 = 0
nBlinks = 75
for iBlink in range(nBlinks):
    stones = blink(stones)
    if iBlink == 24: resultsPart1 = sum([n for _,n in stones.items()])
        
resultsPart2 = sum([n for _ , n in stones.items()])

#%%%# print results #%%#
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {time.time()-t0:.3f} sec')