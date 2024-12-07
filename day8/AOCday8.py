# -*- coding: utf-8 -*-
"""
Advent of Code day 8 script
author: g.osnabrugge
"""
#import numpy as np
import time

#%%# helper functions #%%#

#%%# readout puzzle input file #%%#
# # extract all contents of input file
# inputs = open('input.txt').read()

# # extract entrees per puzzle line
# for line in open('input.txt'):
#     entrees = list(map(int,line.split(' ')))

# # readout puzzle txt file into separate string lines (without white spaces)
# with open('input.txt') as file:
#     lines = [line.rstrip() for line in file]

#%%%# Part 1 #%%#
t0 = time.time()
resultsPart1 = 0


#%%%# Part 2 #%%#
resultsPart2 = 0

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
