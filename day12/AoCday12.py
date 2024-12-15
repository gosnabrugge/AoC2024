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
    nSides = 0
    grid[pos[0]][pos[1]] = '.'
    fencesSet = [[False]*4] # keeps track which fences have already been started before
    for i, plant in enumerate(plantsInRegion):
        row = plant[0]
        col = plant[1]
        newPlants = 0
        
        # first check for borders if fences are needed      
        fences = [False]*4
        if not [row-1,col] in plantsInRegion: # check up
            if row > 0 and grid[row-1][col] == pType:
                plantsInRegion.append([row-1,col])
                grid[row-1][col] = '.'
                area+=1
                newPlants += 1
            else: 
                perimeter += 1
                fences[0] = True
                if not fencesSet[i][0]: nSides += 1
        if not [row,col+1] in plantsInRegion: # check right
            if col < len(grid[0])-1 and grid[row][col+1] == pType:
                plantsInRegion.append([row,col+1])
                grid[row][col+1] = '.'
                area+=1
                newPlants += 1
            else: 
                perimeter += 1
                fences[1] = True
                if not fencesSet[i][1]: nSides += 1
        if not [row+1,col] in plantsInRegion: # check down
            if row < len(grid)-1 and grid[row+1][col] == pType:
                plantsInRegion.append([row+1,col])
                grid[row+1][col] = '.'
                area+=1
                newPlants += 1
            else: 
                perimeter += 1
                fences[2] = True
                if not fencesSet[i][2]: nSides += 1
        if not [row,col-1] in plantsInRegion: # check left
            if col > 0 and grid[row][col-1] == pType:
                plantsInRegion.append([row,col-1])
                grid[row][col-1] = '.'
                area+=1
                newPlants += 1
            else: 
                perimeter += 1
                fences[3] = True
                if not fencesSet[i][3]: nSides += 1
        
        # add fences to set
        for iPlant in range(newPlants): fencesSet.append(fences)
            
        
    cost = area*perimeter
    cost2 = area*nSides
    return grid, cost, cost2
        

#%%# readout puzzle input file #%%#
garden = loadData('test.txt')
nRows = len(garden)
nCols = len(garden[0])

#%%%# Part 1 & 2 #%%#
resultsPart1 = 0
resultsPart2 = 0
gardenPart1 = garden.copy()
for i in range(nRows):
    for j in range(nCols):
        if not gardenPart1[i][j] == '.':
            gardenPart1, cost, cost2 = fence(gardenPart1,[i,j])
            resultsPart1 += cost
            resultsPart2 += cost2

#%%%# print results #%%#
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {time.time()-t0:.3f} sec')