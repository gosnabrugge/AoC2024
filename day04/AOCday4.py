# -*- coding: utf-8 -*-
"""
Advent of Code day 4 script
"""
#### helper functions ####
def grabWord(lines, rowInds, colInds):
    word = ''
    for i in range(len(rowInds)):
        word += lines[rowInds[i]][colInds[i]]
    return word

def checkWordPart1(lines, rowInds, colInds):
    word = grabWord(lines, rowInds, colInds)
    if word == 'XMAS' or word == 'SAMX': return 1
    else: return 0
        
def checkWordPart2(lines, rowInds, colInds):
    word = grabWord(lines, rowInds, colInds)
    if word == 'MAS' or word == 'SAM': return True
    else: return False

#### read input file ####
# readout puzzle txt file into separate lines
with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    
# determine puzzle size
Nrows = len(lines)
Ncols = len(lines[0])

#### Part 1 ####
resultsPart1 = 0
for i in range(Nrows):
    for j in range(Ncols):
        ### check in line characters
        if j <= Ncols-4: # check left to right
            resultsPart1 += checkWordPart1(lines,[i,i,i,i],[j,j+1,j+2,j+3])

        if i <= Nrows-4 and j <= Ncols-4: # check top-left to right-down
            resultsPart1 += checkWordPart1(lines,[i,i+1,i+2,i+3],[j,j+1,j+2,j+3])
            
        if i <= Nrows-4: # check up to down
            resultsPart1 += checkWordPart1(lines,[i,i+1,i+2,i+3],[j,j,j,j])
        
        if i <= Nrows-4 and j >= 3: # check top-right to left-down
            resultsPart1 += checkWordPart1(lines,[i,i+1,i+2,i+3],[j,j-1,j-2,j-3])

        
print('Part 1: '+ str(resultsPart1))

#### Part 2 ####
resultsPart2 = 0
for i in range(1,Nrows-1):
    for j in range(1,Ncols-1):  
        if checkWordPart2(lines,[i-1,i,i+1],[j-1,j,j+1]):     # check diagonal
            if checkWordPart2(lines,[i-1,i,i+1],[j+1,j,j-1]): # check anti-diagonal
                resultsPart2 += 1

print('Part 2: '+ str(resultsPart2))