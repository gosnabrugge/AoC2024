# -*- coding: utf-8 -*-
"""
Advent of Code day 2 script
"""
import numpy as np

# helper functions
def ReportIsSafe(report):
    # compute difference between report numbers
    report = np.array(report)
    reportLen = len(report)
    reportDiff = report[1:reportLen] - report[0:reportLen-1]
    
    # check if report is safe
    reportIsSafe = False
    if max(abs(reportDiff)) <= 3: # check if no numbers changes more than 3
        if sum(reportDiff > 0) == reportLen-1: # check if all numbers are ascending
                reportIsSafe = True
        if sum(reportDiff < 0) == reportLen-1: # check if all numbers are descending
                reportIsSafe = True
                
    return reportIsSafe
    
    
#### Part 1 ####
NsafeReports1 = 0
for line in open('input.txt'):
    # readout report
    report = line.split(" ")
    report = list(map(int,report))
    if ReportIsSafe(report): NsafeReports1 += 1
    

print('Part 1: '+str(NsafeReports1))

#### Part 2 ####
NsafeReports2 = 0
for line in open('input.txt'):
    # readout report
    report = line.split(" ")
    report = list(map(int,report))
    
    if ReportIsSafe(report): 
        NsafeReports2 += 1
    else:
        # check dampened report safety
        for iNum in range(len(report)):
            dampenedReport = report[0:iNum]+report[iNum+1::]
            if ReportIsSafe(dampenedReport): 
                NsafeReports2 += 1
                break

print('Part 2: '+str(NsafeReports2))