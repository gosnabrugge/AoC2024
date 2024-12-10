# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day .. script
author: g.osnabrugge
"""
import numpy as np
import time
t0 = time.time()

#%%# helper functions #%%#
def findTrails(trailHead, grid, requirement):
    gridSize = grid.shape
    trails = [trailHead]
    for iStep in range(9):
        grid -= 1
        nextTrails = []
        for iTrail in range(len(trails)):
            row = trails[iTrail][0]
            col = trails[iTrail][1]
            if row-1 >= 0 and grid[row-1,col] == 0: # check up
                nextTrails.append([row-1,col])
            if col+1 < gridSize[1] and grid[row,col+1] == 0: # check right
                nextTrails.append([row,col+1])
            if row+1 < gridSize[0] and grid[row+1,col] == 0: # check down
                nextTrails.append([row+1,col])
            if col-1 >= 0 and grid[row,col-1] == 0: # check left
                nextTrails.append([row,col-1])
        
        
        if requirement == 'score':
            # only keep unique trail spaces (part 1)
            trails = []
            for nextSpace in nextTrails:
                if not nextSpace in trails:
                    trails.append(nextSpace)
        elif requirement == 'rating':
            # keep all potential trials (part 2)
            trails = nextTrails
    
    # check number of valid trails
    nTrails = len(trails)
    return nTrails

#%%# readout puzzle input file #%%#
inputFile = 'input.txt'

# readout puzzle txt file into separate string lines (without white spaces)
with open(inputFile) as file:
    lines = [line.rstrip() for line in file]

nRows = len(lines)
nCols = len(lines[0])
grid = np.zeros([nRows,nCols],dtype=int)
for i in range(nRows):
    for j in range(nCols):
        grid[i,j] = int(lines[i][j])

#%%%# Part 1 & 2 #%%#
resultsPart1 = 0
resultsPart2 = 0
for i in range(nRows):
    for j in range(nCols):
        # look for trailhead
        if grid[i,j] == 0:
            trailHead = [i,j]
            resultsPart1 += findTrails(trailHead, grid.copy(),'score')
            resultsPart2 += findTrails(trailHead, grid.copy(),'rating')
            
#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
