# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 12 script
author: g.osnabrugge
"""
#import numpy as np
# from collections import defaultdict
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile):
    with open(inputFile) as file:
        return [list(line.rstrip()) for line in file]

def fence(grid,pos):
    pType = grid[pos[0]][pos[1]]
    plantsInRegion = [[pos[0],pos[1]]]
    area = 1
    perimeter = 0
    grid[i][j] = '.'
    for plant in plantsInRegion:
        row = plant[0]
        col = plant[1]
        if not [row-1,col] in plantsInRegion: # check up
            if row > 0 and grid[row-1][col] == pType:
                plantsInRegion.append([row-1,col])
                grid[row-1][col] = '.'
                area+=1
            else: perimeter += 1
        if not [row,col+1] in plantsInRegion: # check right
            if col < len(grid[0])-1 and grid[row][col+1] == pType:
                plantsInRegion.append([row,col+1])
                grid[row][col+1] = '.'
                area+=1
            else: perimeter += 1
        if not [row+1,col] in plantsInRegion: # check down
            if row < len(grid)-1 and grid[row+1][col] == pType:
                plantsInRegion.append([row+1,col])
                grid[row+1][col] = '.'
                area+=1
            else: perimeter += 1
        if not [row,col-1] in plantsInRegion: # check left
            if col > 0 and grid[row][col-1] == pType:
                plantsInRegion.append([row,col-1])
                grid[row][col-1] = '.'
                area+=1
            else: perimeter += 1
    
    cost = area*perimeter
    return grid, cost
        

#%%# readout puzzle input file #%%#
garden = loadData('test.txt')
nRows = len(garden)
nCols = len(garden[0])

#%%%# Part 1 #%%#
resultsPart1 = 0
gardenPart1 = garden.copy()
for i in range(nRows):
    for j in range(nCols):
        if not gardenPart1[i][j] == '.':
            gardenPart1, cost = fence(gardenPart1,[i,j])
            resultsPart1 += cost

#%%%# Part 2 #%%#
resultsPart2 = 0

#%%%# print results #%%#
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {time.time()-t0:.3f} sec')