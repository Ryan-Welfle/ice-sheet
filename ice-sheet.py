#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:41:57 2021

@author: ryanwelfle
"""

#import matplotlib
#matplotlib.use('TkAgg')  #puts plot in a separate window, which makes graph move!
import numpy
import matplotlib.pyplot as plt

nGridCenters = 10                                   # number of grid points
totalPlaneWidth = 1000000                           # meters
gridWidth = totalPlaneWidth/nGridCenters            # distance between grid centers

timeStepLength = 100                              # length of each timeStep
totalYears = 15000                               # how many years we want the simulation to run in total (20000)
timeStep = int(totalYears/timeStepLength)       # number of timeSteps to take


flowParam = 10000             # m horizontal / yr
snowFall = 0.5              # m / yr

elevations = numpy.zeros(nGridCenters+2)  # sets up an array of zeros for each elevations (and boundaries)
flows = numpy.zeros(nGridCenters+1)       # sets up an array of zeros for each flow

fig, ax = plt.subplots()        # one axis graph
ax.plot(elevations)             # what to plot on graph
ax.set_ylim([0,4000])      # setting a limit on how high up the y-axis plots data before stopping
plt.show(block=False)           # throw plot on screen and continue on

for iTime in range(0, timeStep):
    for i in range(0, nGridCenters+1):
        flows[i] = (elevations[i]-elevations[i+1])/gridWidth * flowParam * (elevations[i]+elevations[i+1])/2/gridWidth
    for j in range(1, nGridCenters+1):
        elevations[j]+= timeStep*(snowFall+flows[j-1]-flows[j]) #snowFall with flows[j-1] coming/going and flow[j] coming/going depending on side of hill
    projectedYear = iTime*timeStep
    print('year', projectedYear)
    if projectedYear==totalYears:
        break
    ax.clear()
    ax.plot(elevations)
    ax.set_ylim([0,4000])
    plt.show(block=False)
    plt.pause(0.001)
    fig.canvas.draw()
    
print('\nFinished!')
print(f'Highest elevation point is {max(elevations)} m')

