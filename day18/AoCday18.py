# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 18 script
author: g.osnabrugge
"""
import numpy as np
from matplotlib import pyplot as plt
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile,nBytes, gridSize):
    fallingBytes = []
    for lines in open(inputFile):
        coords = lines.split(',')
        fallingBytes.append([int(coords[0]),int(coords[1])])
    
    # generate grid
    grid = np.zeros(gridSize)
    for byte in fallingBytes[0:nBytes]: grid[byte[1],byte[0]] = -1

    return fallingBytes, grid

def findPath(grid):
    pathFound = False
    endPos = [grid.shape[1]-1,grid.shape[0]-1]
    
    # perform first steps
    if grid[1,0] == 0: grid[1,0] = 1
    if grid[0,1] == 0: grid[0,1] = 1
    
    # move to end
    nextStep = 0
    while not pathFound:
        nextStep += 1
        rows, cols = np.where(grid==nextStep)
        
        for ind in range(len(rows)):
            if [rows[ind],cols[ind]] == endPos:
                pathFound = True
                break
            
            # expand path into neighbouring open spaces
            if rows[ind] > 0 and grid[rows[ind]-1,cols[ind]] == 0: grid[rows[ind]-1,cols[ind]] = nextStep+1
            if cols[ind] < grid.shape[1]-1 and grid[rows[ind],cols[ind]+1] == 0: grid[rows[ind],cols[ind]+1] = nextStep+1
            if rows[ind] < grid.shape[0]-1 and grid[rows[ind]+1,cols[ind]] == 0 : grid[rows[ind]+1,cols[ind]] = nextStep+1
            if cols[ind] > 0 and grid[rows[ind],cols[ind]-1] == 0: grid[rows[ind],cols[ind]-1] = nextStep+1
        
        if len(rows) == 0: break # path cannot be found
        
    return nextStep, grid, pathFound
        

#%%# readout puzzle input file #%%#
nBytes = 1024
gridSize = [71,71]
fallingBytes, grid = loadData('input.txt',nBytes,gridSize)

# # test case
# nBytes = 12
# gridSize = [7,7]
# fallingBytes, grid = loadData('test.txt',nBytes,gridSize)

#%%%# Part 1 #%%#
resultsPart1, gridPath, pathFound = findPath(grid.copy())

#%%%# Part 2 #%%#
resultsPart2 = 0
iByte = nBytes-1
while pathFound:
    iByte += 1
    byte = fallingBytes[iByte]
    grid[byte[1],byte[0]] = -1
    _, _, pathFound = findPath(grid.copy())

resultsPart2 = byte

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2[0]) + ',' + str(resultsPart2[1]))
print(f'runtime: {tTot:.3f} sec')
