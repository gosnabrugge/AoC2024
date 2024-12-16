# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day .. script
author: g.osnabrugge
"""
import numpy as np
from matplotlib import pyplot as plt
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile):
    with open(inputFile) as file: lines = [line.rstrip() for line in file]
    
    nRows = len(lines)
    nCols = len(lines[0])
    dirGrid = np.zeros([nRows,nCols], dtype=int)
    stepsGrid = np.zeros([nRows,nCols], dtype=int) # tracks last directions taken (1:up, 2:right, 3:down, 4:left, 9:end, -1:obstacle)
    for i in range(nRows):
        for j in range(nCols):
            if lines[i][j] == '#': 
                dirGrid[i,j] = -1
                stepsGrid[i,j] = -1
            elif lines[i][j] == 'S': # perform first step
                dirGrid[i,j] = 2
                if lines[i-1][j] == '.': # move north
                    stepsGrid[i-1,j] = 1001
                    dirGrid[i-1,j] = 1
                if lines[i][j+1] == '.': # move east
                     stepsGrid[i,j+1] = 1
                     dirGrid[i,j+1] = 2
                if lines[i+1][j] == '.': # move east
                     stepsGrid[i+1,j] = 1001
                     dirGrid[i+1,j] = 3        
            
    return stepsGrid, dirGrid, lines

def nextStep(steps, grid, pos):
    i = int(pos[0])
    j = int(pos[1])
        
    # fill in next spaces
    if grid[i,j] == 1: # move north
        if not grid[i,j-1] == -1 or grid[i,j-1] > steps[i,j]+1001:
            grid[i,j-1] = 4
            steps[i,j-1] = steps[i,j]+1001
        if grid[i-1,j] == 0 or steps[i-1,j] > steps[i,j]+1:
            grid[i-1,j] = 1
            steps[i-1,j] = steps[i,j]+1
        if grid[i,j+1] == 0 or steps[i,j+1] > steps[i,j]+1001:
            grid[i,j+1] = 2
            steps[i,j+1] = steps[i,j]+1001
            
    if grid[i,j] == 2: # move east
        if grid[i-1,j] == 0 or steps[i-1,j] > steps[i,j]+1001:
            grid[i-1,j] = 1
            steps[i-1,j] = steps[i,j]+1001
        if grid[i,j+1] == 0 or steps[i,j+1] > steps[i,j]+1:
            grid[i,j+1] = 2
            steps[i,j+1] = steps[i,j]+1
        if grid[i+1,j] == 0 or steps[i+1,j] > steps[i,j]+1001:
            grid[i+1,j] = 3
            steps[i+1,j] = steps[i,j]+1001
            
    if grid[i,j] == 3: # move south
        if grid[i,j+1] == 0 or steps[i,j+1] > steps[i,j]+1001:
            grid[i,j+1] = 2
            steps[i,j+1] = steps[i,j]+1001
        if grid[i+1,j] == 0 or steps[i+1,j] > steps[i,j]+1:
            grid[i+1,j] = 3
            steps[i+1,j] = steps[i,j]+1
        if grid[i,j-1] == 0 or steps[i,j-1] > steps[i,j]+1001:
            grid[i,j-1] = 4
            steps[i,j-1] = steps[i,j]+1001
            
    if grid[i,j] == 4: # move west
        if grid[i+1,j] == 0 or steps[i+1,j] > steps[i,j]+1001:
            grid[i+1,j] = 3
            steps[i+1,j] = steps[i,j]+1001
        if grid[i,j-1] == 0 or steps[i,j-1] > steps[i,j]+1:
            grid[i,j-1] = 4
            steps[i,j-1] = steps[i,j]+1
        if grid[i-1,j] == 0 or steps[i-1,j] > steps[i,j]+1001:
            grid[i-1,j] = 1
            steps[i-1,j] = steps[i,j]+1001
    
    return steps, grid

#%%# readout puzzle input file #%%#
steps, grid, lines = loadData('input.txt')

#%%%# Part 1 #%%#
resultsPart1 = 0
endFound = False
prevNum = 0
while not endFound:
    # find next smallest number of steps
    nextNum = np.sort(steps[steps>prevNum])[0]
    rows, cols = np.where(steps == nextNum)
    
    for ind in range(len(rows)):
        pos = [rows[ind], cols[ind]]
        if lines[pos[0]][pos[1]] == 'E':
            resultsPart1 = steps[pos[0],pos[1]]
            endFound = True
            break
        
        steps, grid = nextStep(steps, grid, pos)
        # plt.imshow(steps)
        # plt.show()
        
    prevNum = nextNum

plt.imshow(steps)
plt.show()


#%%%# Part 2 #%%#
resultsPart2 = 0

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
