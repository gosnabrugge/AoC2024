# -*- coding: utf-8 -*-
"""
Advent of Code 2024 day 14 script
author: g.osnabrugge
"""
import numpy as np
import math
import copy
import time
from matplotlib import pyplot as plt
t0 = time.time()

#%%# helper functions #%%#

#%%# readout puzzle input file #%%#
def loadData(inputFile):
    # read out positions and velocities of robots
    robots = []
    for line in open(inputFile):
        robot = [0,0,0,0]
        ind1 = line.find(',')
        ind2 = line.find('v=')
        ind3 = line.find(',',ind2)
        robot[0] = int(line[2:ind1])
        robot[1] = int(line[ind1+1:ind2-1])
        robot[2] = int(line[ind2+2:ind3])
        robot[3] = int(line[ind3+1::])
        robots.append(robot)
    return robots

def move(robot, t, roomSize):
    robot[0] = (robot[0] + robot[2]*t)%roomSize[0]
    robot[1] = (robot[1] + robot[3]*t)%roomSize[1]
    return robot
    
def calculateSecurityScore(robots, t, roomSize):
    # determines security score of bathroom state after t seconds
    quadBorder = [math.floor(roomSize[0]/2), math.floor(roomSize[1]/2)]
    quadrants = [0,0,0,0]
    for robot in robots:
        robot = move(robot, t, roomSize)
        
        if   robot[0] < quadBorder[0] and robot[1] < quadBorder[1]: quadrants[0] += 1     
        elif robot[0] < quadBorder[0] and robot[1] > quadBorder[1]: quadrants[1] += 1
        elif robot[0] > quadBorder[0] and robot[1] < quadBorder[1]: quadrants[2] += 1
        elif robot[0] > quadBorder[0] and robot[1] > quadBorder[1]: quadrants[3] += 1
    
    securityScore = quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]
    return securityScore

def determineBathroomState(robots, roomSize):
    bathroom = np.zeros(roomSize)
    for robot in robots: bathroom[robot[0],robot[1]] = 1
    
    # determine variance in robot positions
    grid = np.mgrid[0:roomSize[0], 0:roomSize[1]]
    meanPos = (bathroom * grid).sum(1).sum(1)/bathroom.sum()
    
    # create (X-mu)^2 grid (used to calculate position variance)
    varGrid = np.power(np.mgrid[-meanPos[0]:-meanPos[0]+roomSize[0],
                         -meanPos[1]:-meanPos[1]+roomSize[1]],2)
    

    variancePos = (bathroom * varGrid).sum(1).sum(1)/bathroom.sum()
    varianceTot = np.sqrt(variancePos[0]**2+variancePos[1]**2)
    
    return bathroom, varianceTot

#%%# readout puzzle input file #%%#
robots = loadData('input.txt')
roomSize = [101,103]
# robots = loadData('test.txt')
# roomSize = [11,7]

#%%%# Part 1 #%%#
resultsPart1 = calculateSecurityScore(copy.deepcopy(robots), 100, roomSize)

#%%%# Part 2 #%%#
# determine starting position variance
_, varStart = determineBathroomState(robots, roomSize)

t = 0
easterEggFound = False
while not easterEggFound:
    # move robots and determine new bathroom state (and check new position variance)
    t += 1
    for robot in robots: robot = move(robot, 1, roomSize)
    
    bathroom, varPattern = determineBathroomState(robots, roomSize)
    if varPattern < (varStart/2):
        plt.imshow(bathroom)
        plt.title(str(t))
        plt.show()
        easterEggFound = True
        
resultsPart2 = t

#%%%# print results #%%#
tTot = time.time()-t0
print('Part 1: '+ str(resultsPart1))
print('Part 2: '+ str(resultsPart2))
print(f'runtime: {tTot:.3f} sec')
