#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:41:57 2021

@author: ryanwelfle
"""

#import matplotlib                                  # puts plot in a separate window
#matplotlib.use('TkAgg')                            # (uncomment matplotlib commands if your environment doesn't do this already)
import numpy
import matplotlib.pyplot as plt

nGridCenters = 10                                   # number of grid points
totalPlaneWidth = 1000000                           # meters
gridWidth = totalPlaneWidth/nGridCenters            # distance between grid centers

timeStepLength = 100                              # length of each timeStep
totalYears = 15000                                # how many years we want the simulation to run in total (20000)
timeStep = int(totalYears/timeStepLength)         # number of timeSteps to take

flowParam = 10000             # m horizontal / yr
snowFall = 0.5                # m / yr

elevations = numpy.zeros(nGridCenters+2)  # sets up an array of zeros for each elevations (and boundaries)
flows = numpy.zeros(nGridCenters+1)       # sets up an array of zeros for each flow

#  Visual:
#  eX = value in "elevations" list (numbered as per index); e0 and e11 always equal zero
#  fX = value in "flows" list (numbered as per index)
#
#| e0=0 |  e1  |  e2  |  e3  |  e4  |  e5  |  e6  |  e7  |  e8  |  e9  |  e10 | e11=0|
#|      |      |      |      |      |      |      |      |      |      |      |      |     
#|     f0     f1     f2     f3     f4     f5     f6     f7     f8     f9     f10     |    
#|      |      |      |      |      |      |      |      |      |      |      |      |    
#| water|  ice |  ice |  ice |  ice |  ice |  ice |  ice |  ice |  ice |  ice | water|   

fig, ax = plt.subplots()        # one axis graph
ax.plot(elevations)             # what to plot on graph
plt.xticks(numpy.arange(0, 11, 1))
ax.set_ylim([0,4000])           # setting a limit on how high up the y-axis plots data before stopping
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
    plt.xticks(numpy.arange(0, 11, 1))
    ax.set_ylim([0,4000])
    plt.show(block=False)
    plt.pause(0.1)
    fig.canvas.draw()
    
print('\nFinished!')
print(f'Highest elevation point is {max(elevations)} m.\n')

