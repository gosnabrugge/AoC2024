# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day .. script
author: g.osnabrugge
"""
#import numpy as np
import time
t0 = time.time()

#%%# helper functions #%%#

#%%# readout puzzle input file #%%#
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


#%%%# Part 2 #%%#
resultsPart2 = 0

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
