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
    ## find all plants in region
    pType = grid[pos[0]][pos[1]]
    plantsInRegion = [[pos[0],pos[1]]]
    for i, plant in enumerate(plantsInRegion):
        row = plant[0]
        col = plant[1]
    
        if row > 0 and grid[row-1][col] == pType and not [row-1,col] in plantsInRegion: 
            plantsInRegion.append([row-1,col]) # add upper neighbour
        if col < len(grid[0])-1 and grid[row][col+1] == pType and not [row,col+1] in plantsInRegion: 
            plantsInRegion.append([row,col+1]) # add right neighbour
        if row < len(grid)-1 and grid[row+1][col] == pType and not [row+1,col] in plantsInRegion:
            plantsInRegion.append([row+1,col]) # add lower neighbour
        if col > 0 and grid[row][col-1] == pType and not [row,col-1] in plantsInRegion: 
            plantsInRegion.append([row,col-1]) # add left neighbour
    
    area = len(plantsInRegion) 
    
    # check total size of region
    rows = [plant[0] for plant in plantsInRegion]
    cols = [plant[1] for plant in plantsInRegion]
    
    ## find perimeter and number of sides of region
    nSides = 0
    perimeter = 0
    
    # find all vertical sides of region (checks all rows for edges)
    startEdges = []
    endEdges = []
    inRegion = False
    for i in range(min(rows),max(rows)+1):
        # list to track which sides have been found before
        prevStartEdges = startEdges
        prevEndEdges = endEdges
        startEdges = []
        endEdges = []
        
        for j in range(min(cols),max(cols)+1):
            if [i,j] in plantsInRegion and not inRegion:
                startEdges.append(j)
                inRegion = True
            elif not [i,j] in plantsInRegion and inRegion:
                endEdges.append(j)
                inRegion = False
            
            if j == max(cols) and inRegion: # if last space was in region then end with fence
                endEdges.append(j+1)
                inRegion = False
        
        # determine perimeter and number of sides
        perimeter += len(startEdges) + len(endEdges)
        for edge in startEdges: 
            if not edge in prevStartEdges: nSides += 1
        for edge in endEdges: 
            if not edge in prevEndEdges: nSides += 1
        
    # find all horizontal sides of region (checks all columns for edges)
    startEdges = []
    endEdges = []
    inRegion = False
    for j in range(min(cols),max(cols)+1):
        # list to track which sides have been found before
        prevStartEdges = startEdges
        prevEndEdges = endEdges
        startEdges = []
        endEdges = []
        for i in range(min(rows),max(rows)+1):
            if [i,j] in plantsInRegion and not inRegion:
                startEdges.append(i)
                inRegion = True
            elif not [i,j] in plantsInRegion and inRegion:
                endEdges.append(i)
                inRegion = False
            
            if i == max(rows) and inRegion: # if last space was in region then end with fence
                endEdges.append(i+1)
                inRegion = False
        
        # determine perimeter and number of sides
        perimeter += len(startEdges) + len(endEdges)
        for edge in startEdges: 
            if not edge in prevStartEdges: nSides += 1
        for edge in endEdges: 
            if not edge in prevEndEdges: nSides += 1
        
        

    # remove all plant spaces in region from grid
    for plant in plantsInRegion: grid[plant[0]][plant[1]] = '.'
    
    cost = area*perimeter
    cost2 = area*nSides
    return grid, cost, cost2
        

#%%# readout puzzle input file #%%#
garden = loadData('input.txt')
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