# -*- coding: utf-8 -*-
"""
Advent of Code day 3 script
"""
#import numpy as np    
#import re
    
def checkInstruction(instruction):
    # find end of instruction
    endInd = instruction.find(')')         
    if endInd == -1: return 0
    
    # extract inputs from substring
    inputs = instruction[4:endInd]
    inputs = inputs.split(',')
    
    # reject if more than 2 numbers are inserted
    if len(inputs) != 2: return 0 
    
    # reject if inputs contain spaces
    indX = inputs[0].find(' ')
    indY = inputs[1].find(' ')
    if indX != -1 or indY != -1: return 0
    
    # check if inputs can be converted to integers
    try: 
        X = int(inputs[0])
        Y = int(inputs[1])
        if abs(X) >= 1e3 or abs(Y) >= 1e3: 
            return 0
        else: # instruction is valid
            return X*Y
    except:
        return 0

# read whole txt file as single string
inputTxt = open('input.txt').read()   

#### Part 1 ####
results1 = 0     # results variable
eof = False
ind = -1
while not eof:
    # check line for target substring
    ind = inputTxt.find('mul(',ind+1)
    
    if ind == -1:
        eof = True
    else:
        instruction = inputTxt[ind:ind+12]
        output = checkInstruction(instruction)
        results1 += output

""" solution using regular expressions:
pattern = r"mul\(\d+.\d+\)"
matches = re.findall(pattern, open('input.txt').read())
"""            
    
print('Part 1: '+ str(results1))

#### Part 2 ####

results2 = 0      # results variable
eof = False
ind = -1
dontInd = inputTxt.find("don't()", 0)

while not eof:
    # check line for target substring
    ind = inputTxt.find('mul(',ind+1)
   
    if ind>dontInd and dontInd != -1:
       ind = inputTxt.find("do()",dontInd)     # skip to the next do() command
       dontInd = inputTxt.find("don't()", ind) # update don't() command
       
    if ind == -1: 
        eof = True
    else:
        instruction = inputTxt[ind:ind+12]
        output = checkInstruction(instruction)            
        results2 += output

""" solution using regular expressions:
pattern = r"mul\(\d+.\d+\)"
matches = re.findall(pattern, open('input.txt').read())
""" 

print('Part 2: '+ str(results2))