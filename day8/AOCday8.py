# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 8 script 
author: g.osnabrugge
"""
import numpy as np
import time
t0 = time.time()

#%%# readout puzzle input file #%%#
# readout puzzle txt file into separate string lines (without white spaces)
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

nRows = len(lines)
nCols = len(lines[0])

# collect all attena locations in dictionary
attenaList = dict()
for i in range(nRows):
    for j in range(nCols):
        key = lines[i][j]
        if not key == '.':
            if key in attenaList: # add entree coordinates to dictionary
                attenaList[key].append([i,j])
            else: # create new entree in dictionary
                attenaList[key] = [[i,j]]

#%%%# Part 1 #%%#
aNodeGrid = np.zeros([nRows,nCols],dtype=int)

for key in attenaList:
    nAttenas = len(attenaList[key])
    for i in range(nAttenas):
        for j in range(nAttenas):
            if not i == j:
                iAttena = attenaList[key][i]
                jAttena = attenaList[key][j]
                aNodeRow = iAttena[0] + 2*(jAttena[0]-iAttena[0])
                aNodeCol = iAttena[1] + 2*(jAttena[1]-iAttena[1])
                nodeOnGrid = (aNodeRow >= 0 and aNodeRow < nRows) and (aNodeCol >= 0 and aNodeCol < nCols)
                if nodeOnGrid:
                    aNodeGrid[aNodeRow,aNodeCol] = 1

resultsPart1 = np.sum(aNodeGrid.flatten())

#%%%# Part 2 #%%#
aNodeGrid2 = np.zeros([nRows,nCols],dtype=int)

for key in attenaList:
    nAttenas = len(attenaList[key])
    for i in range(nAttenas):
        for j in range(nAttenas):
            if not i == j:
                nodeOnGrid = True
                iNode = 0
                while nodeOnGrid:
                    iAttena = attenaList[key][i]
                    jAttena = attenaList[key][j]
                    aNodeRow = iAttena[0] + iNode*(jAttena[0]-iAttena[0])
                    aNodeCol = iAttena[1] + iNode*(jAttena[1]-iAttena[1])
                    nodeOnGrid = (aNodeRow >= 0 and aNodeRow < nRows) and (aNodeCol >= 0 and aNodeCol < nCols)
                    if nodeOnGrid:
                        aNodeGrid2[aNodeRow,aNodeCol] = 1
                        iNode += 1

resultsPart2 = np.sum(aNodeGrid2.flatten())

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
