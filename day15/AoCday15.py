# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 15 script
author: g.osnabrugge
"""
import numpy as np
from matplotlib import pyplot as plt
import time
t0 = time.time()

#%%# helper functions #%%#
def loadData(inputFile, part):
    # # readout puzzle txt file into separate string lines (without white spaces)
    with open(inputFile) as file:
        lines = [line.rstrip() for line in file]
    sepInd = lines.index('') # find line nr separating grid and moves datasets
    
    # generate instructions string
    instructions = ''
    for line in lines[sepInd+1::]: instructions += line
    
    # generate warehouse grid
    linesGrid = lines[0:sepInd]
    nRows = len(linesGrid)
    nCols = len(linesGrid[0])
    
    if part == 1:
        grid = np.zeros([nRows,nCols])
        for i in range(nRows):
            for j in range(nCols):
                if   lines[i][j] == '#': grid[i,j] = -1
                elif lines[i][j] == 'O': grid[i,j] = 1
                elif lines[i][j] == '@': grid[i,j] = 3
    elif part == 2:
        grid = np.zeros([nRows,2*nCols])
        for i in range(nRows):
            for j in range(nCols):
                if   lines[i][j] == '#': grid[i,2*j:2*(j+1)] = [-1,-1]
                elif lines[i][j] == 'O': grid[i,2*j:2*(j+1)] = [1,2]
                elif lines[i][j] == '@': grid[i,2*j:2*(j+1)] = [3,0]
    # generate move instructions string
    moves = ''
    for line in lines[sepInd+1::]: moves += line
    
    return grid, moves

def moveRobot(grid, move):
    # determine robot starting pos
    pos = np.where(grid == 3)
    row = int(pos[0][0])
    col = int(pos[1][0])
    
    # move robot (and push boxes)
    if move == '^':
        row2 = row - 1
        while grid[row2,col] == 1: row2 -= 1 # while encountering boxes
        if grid[row2,col] == 0: 
            grid[row-1:row2-1:-1,col] = grid[row:row2:-1,col]
            grid[row,col] = 0
    elif move == '>':
        col2 = col + 1
        while grid[row,col2] == 1: col2 += 1
        if grid[row,col2] == 0: 
            grid[row,col+1:col2+1] = grid[row,col:col2]
            grid[row,col] = 0
    elif move == 'v':
        row2 = row + 1
        while grid[row2,col] == 1: row2 += 1
        if grid[row2,col] == 0: 
            grid[row+1:row2+1,col] = grid[row:row2,col]
            grid[row,col] = 0
    elif move == '<':
        col2 = col - 1
        while grid[row,col2] == 1: col2 -= 1
        if grid[row,col2] == 0: 
            grid[row,col-1:col2-1:-1] = grid[row,col:col2:-1]
            grid[row,col] = 0
    
    return grid                

def moveWideRobot(grid, move):
    # determine robot starting pos
    pos = np.where(grid == 3)
    row = int(pos[0][0])
    col = int(pos[1][0])
    
    # move robot (and push boxes)
    pushing = True
    gridTmp = grid.copy()
    if move == '^':
        row2 = row-1
        cols = [col]
        gridTmp[row,col] = 0
        while pushing:
            # check all previously pushed collumns            
            colsNext = []
            for col in cols:
                gridTmp[row2,col] = grid[row2+1,col]
                if grid[row2,col] == 1: 
                    colsNext += [col,col+1]
                    if grid[row2+1,col] == 2 or grid[row2+1,col] == 3: gridTmp[row2,col+1] = 0
                    gridTmp[row2-1,[col,col+1]] = [1,2]
                elif grid[row2,col] == 2: 
                    colsNext += [col-1,col]
                    if (grid[row2+1,col] == 1 and not col-1 in cols) or grid[row2+1,col] == 3: gridTmp[row2,col-1] = 0
                    gridTmp[row2-1,[col-1,col]] = [1,2]
            
            # check if still pushing
            if any(grid[row2,cols] == -1): pushing = False # encountered wall
            elif all(grid[row2,cols] == 0):
                pushing = False
                grid = gridTmp
            else:
                cols = list(set(colsNext))
                row2 -= 1
            
            
    elif move == 'v':
        row2 = row+1
        cols = [col]
        gridTmp[row,col] = 0
        while pushing:
            # check all previously pushed collumns            
            colsNext = []
            for col in cols:
                gridTmp[row2,col] = grid[row2-1,col]
                if grid[row2,col] == 1: 
                    colsNext += [col,col+1]
                    if grid[row2-1,col] == 2 or grid[row2-1,col] == 3: gridTmp[row2,col+1] = 0
                    gridTmp[row2+1,[col,col+1]] = [1,2]
                elif grid[row2,col] == 2: 
                    colsNext += [col-1,col]
                    if (grid[row2-1,col] == 1 and not col-1 in cols) or grid[row2-1,col] == 3: gridTmp[row2,col-1] = 0
                    gridTmp[row2+1,[col-1,col]] = [1,2]
            
            # check if still pushing
            if any(grid[row2,cols] == -1): pushing = False # encountered wall
            elif all(grid[row2,cols] == 0):
                pushing = False
                grid = gridTmp
            else:
                cols = list(set(colsNext))
                row2 += 1
    

    elif move == '>':
        col2 = col + 1
        while grid[row,col2] == 1 or grid[row,col2] == 2: col2 += 1
        if grid[row,col2] == 0: 
            grid[row,col+1:col2+1] = grid[row,col:col2]
            grid[row,col] = 0
        
    elif move == '<': 
        col2 = col - 1
        while grid[row,col2] == 1 or grid[row,col2] == 2: col2 -= 1
        if grid[row,col2] == 0: 
            grid[row,col-1:col2-1:-1] = grid[row,col:col2:-1]
            grid[row,col] = 0
    
    return grid   

def calculateGPSsum(grid):
    GPSsum = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] == 1: GPSsum += 100*i+j
    return GPSsum
    
#%%%# Part 1 #%%#
grid1, moves = loadData('input.txt',1)

for iStep in range(len(moves)):
    grid1 = moveRobot(grid1, moves[iStep])
    # plt.imshow(grid1)
    # plt.title(str(iStep+1)+': '+moves[iStep])
    # plt.show()

resultsPart1 = calculateGPSsum(grid1)

#%%%# Part 2 #%%#
resultsPart2 = 0
grid2, moves = loadData('input.txt',2)
plt.imshow(grid2)
plt.title('start')
plt.show()
time.sleep(0.5)

for iStep in range(len(moves)):
    grid2 = moveWideRobot(grid2, moves[iStep])
    
plt.imshow(grid2)
plt.title(str(iStep+1)+': '+moves[iStep])
plt.show()

resultsPart2 = calculateGPSsum(grid2)

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
