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

nElevationCenters = 10                                   # number of grid points
totalPlaneWidth = 1000000                                # meters
subPlaneWidth = totalPlaneWidth/nElevationCenters        # distance between grid centers

timeStepLength = 100                              # length of each timeStep
totalYears = 13000                                # how many years we want the simulation to run in total (20000)
timeStep = int(totalYears/timeStepLength)         # number of timeSteps to take

snowFall = 0.5                # m / yr
flowParam = 10000             # horizontal "movement" of snow / yr

elevations = numpy.zeros(nElevationCenters+2)  # sets up an array of zeros for each elevations (and boundaries)
flows = numpy.zeros(nElevationCenters+1)       # sets up an array of zeros for each flow

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
plt.title(f"Ice Sheet Simulator", fontsize= 20, weight='bold')
plt.xlabel("Elevation Points (0 and 11 represent water)")
plt.ylabel("Elevation in Meters")
plt.xticks(numpy.arange(0, 12, 1))
ax.set_ylim([0,4000])           # setting a limit on how high up the y-axis plots data
plt.show(block=False)           # throw plot on screen and continue on

for step in range(0, timeStep):
    for i in range(0, nElevationCenters+1):
        flows[i] = (elevations[i]-elevations[i+1])/subPlaneWidth * flowParam * (elevations[i]+elevations[i+1])/2/subPlaneWidth
    for j in range(1, nElevationCenters+1):
        elevations[j]+= timeStepLength*(snowFall+flows[j-1]-flows[j]) #snowFall with flows[j-1] coming/going and flow[j] coming/going depending on side of hill
    currentYear = step*timeStepLength
    print('year', currentYear)
    if currentYear==totalYears:
        break
    ax.clear()
    ax.plot(elevations)
    plt.xticks(numpy.arange(0, 12, 1))
    plt.title(f"Ice Sheet Simulator", fontsize=20, weight='bold')
    plt.xlabel("Elevation Points (0 and 11 represent water)")
    plt.ylabel("Elevation in Meters")
    ax.set_ylim([0,4000])
    plt.show(block=False)
    plt.pause(0.1)
    fig.canvas.draw()

print('year', currentYear+timeStepLength)   
print('\nFinished!')
print(f'Highest elevation point is {max(elevations)} m.\n')

