# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 9 script
author: g.osnabrugge
"""
#import numpy as np
import time
t0 = time.time()

#%%# helper functions #%%#

#%%# readout puzzle input file #%%#
# extract all contents of input file
inputs = open('input.txt').read()
# inputs = '2333133121414131402'
# inputs = '12345'

#%%%# Part 1 #%%#
# unpack IDs and empty spaces
inputsUnpacked = []
containsData = 0

for i in range(len(inputs)):
    if inputs[i] == '\n': break
    digit = int(inputs[i])
    containsData = (containsData+1)%2
    if containsData:
        ID = int(i/2)
        inputsUnpacked += [ID]*digit
    else:
        inputsUnpacked += ['.']*digit

# compress dataset
i = 0    # forward counter
j = -1   # backwards counter
inputsCompressed = inputsUnpacked.copy()
while i <= len(inputsUnpacked)+j:
    if inputsUnpacked[i] == '.':
        while inputsUnpacked[j] == '.': j -= 1
        if i <= len(inputsUnpacked)+j:
            inputsCompressed[i] = inputsUnpacked[j]
            inputsCompressed[j] = '.'
            j -= 1
    i += 1

# compute check sum
resultsPart1 = 0
for i in range(len(inputsCompressed)):
    if not inputsCompressed[i] == '.':
        resultsPart1 += i*inputsCompressed[i]

#%%%# Part 2 #%%#
# compress disk using 2nd method
i = 0    # forward counter
j = -1   # backwards counter
inputsCompressed2 = inputsUnpacked.copy()
compressionComplete = False
while not compressionComplete:
    # search for file block (in backwards order)
    while inputsUnpacked[j] == '.' and not compressionComplete: 
        j -= 1
        if inputsUnpacked[j] == 0: #Note: first block is always ID 0
            compressionComplete = True
    
    # check data file length
    if compressionComplete: break
    jStart = j
    while inputsUnpacked[j] == inputsUnpacked[jStart]: j -= 1
    lenFileBlock = jStart-j

    # search for empty span with sufficient length (forward search)
    i = 0
    searchComplete = False
    while not searchComplete:
        # find start of next empty span
        while not inputsCompressed2[i] == '.': 
            i += 1
            if not i <= len(inputsUnpacked)+j:
                searchComplete = True
                break
        if searchComplete: break
    
        # check empty span length
        iStart = i
        while inputsCompressed2[i] == '.': i += 1
        lenEmptySpan = i-iStart
            
        if lenEmptySpan >= lenFileBlock:
            # move file block to new location
            inputsCompressed2[iStart:iStart+lenFileBlock] = inputsCompressed2[jStart:j:-1]
            inputsCompressed2[jStart:j:-1] = '.'*lenFileBlock
            searchComplete = True
        i += 1

# compute check sum
resultsPart2 = 0
for i in range(len(inputsCompressed2)):
    if not inputsCompressed2[i] == '.':
        resultsPart2 += i*inputsCompressed2[i]

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
