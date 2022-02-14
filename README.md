# Welcome to my Ice Sheet Simulator

This is a program based on the "Simple 1-D Ice Sheet Flow Model" that is a part of the "Global Warming II: Create You Own Models in Python" Coursera course, provided by the University of Chicago.

The main output of this program is a moving pseudo-bell-curve graph that simulates the elevation-growth of a sheet of ice on a 1,000,000 meter-wide (1-dimensional) flat plane. 

The simulated plane is flanked by two patches of water (not unlike a larger landmass like Greenland), and it gains its ice from 0.5 meters of "snowfall" per year. As the ice accrues in the simulation, an "ice hill" develops based on continous snowfall raising the elevation of settled ice, and ice slowly "flows" downhill into the surrounding water (as dictated by a flow equation, etc.).

The main point of this program is to give a sped-up and simplified visual of the specific way that ice accrues, and flows down itself.

## A break-down of how the program operates

**Setting up variables to represent elevation points, and plane dimensions (for the purposes of future calculations):**
* ten "elevation points" are set up with the "nElevationCenters" variable, to set the number of changing elevation points needed for the simulation 
* the total width of the flat plane that the snow will fall on is defined with the "totalPlaneWidth" (set to 1,000,000 meters)
* this flat plane is divided by the "nElevationCenters" variable to divide the plane into ten equal widths (one part for each "elevation point"); the resulting number is stored in the "subPlaneWidth" variable; for a mental visual on this, imagine that each "elevation point" resides at the center of each "subPlaneWidth"

**Setting up variables to represent time iterations (for the purposes of future calculations):**
* the simulation displays itself visually by constantly resetting values in graph-form, like a flip-book; each new iteration of the graph simulates a time-step
* the length of each time-step is defined by the "timeStepLength" variable (100 years)
* the total number of years that the simulation will run for is set by the "totalYears" variable; this is set to "13000 years", mostly because this is where the simulation "levels" out based on all of the other inputs
* the number of time-steps taken is calculated by dividing "totalYears" by "timeStepLength"

**Setting up variables to represent snow/ice movement (for the purposes of future calculations):**
* the "snowFall" variable holds a number representing meters of simulated snow that falls each year (0.5 meters) 
* the "flowParam" holds a "flow constant" number (10,000) that helps govern and account for "horizonal" ice-flow "downhill" between elevation points; this is a constant provided by the original course instructor to input into the "flow equation" used later in the program to better simulate the flow of ice (by accounting for the aspect-ratio of the graph)

**Setting up lists to hold elevation and flow values (for the purposes of future calculations):**
* two lists of multiple zeros are calculated: an "elevations" list (that we will use to collect and plot elevations centers), and a "flows" list (that we will use to collect flow values, and use them to iteratively change elevation centers)
* the number of items in the "elevations" list is equal to "nElevationCenters+2" so that we have "elevations" values for each elevation center, as well as an extra 2 to represent "water" points (that will always have zero elevation) that flank the elevation centers
* the number of items in the "flows" list is equal to "nElevationCenters+1" so that we have "flow" items that exist "in between" adjacent elevation points (or between an elevation point and water point where applicable)
* the zeros in these lists are placeholders for future values
* *a visual of "where" flows points are "located" in relation to elevation/water points can be seen as comments after these list initializations* 

**Setting up and showing the initial graph iteration for the simulation**
* a one-axis graph is initalized with "fig, ax = plt.subplots()"
* the axis is set to display the values in the "elevations" list; a pertinent graph title, and axis labels are set up as well
* "plt.xticks" is set up so that the x-axis increments by 1, so that users can more clearly see where each elevation point is located on the graph
* the "y-limit" is set to not exceed 4000 meters, since in this program we are not displaying values that exceed 4000 meters
* we set "plt.show()" to "block=False" so that the graph updates without the graph-window needing to be closed to do so
* this first instance of the simulation won't show anything yet, since all "elevation" list values are set to zero

**Creating the for-loop that creates and displays the rest of the iterations of the simulation**

*Each iteration of the for-loop goes as follows:*

* a for-loop iterates through each item in the "flows" list:
    * each flow item is calculated by first calculating the slope between each adjacent "elevation point" by dividing adjacent "elevation" list-item differences by the "subPlaneWidth" (the distance between those two points)
    * then, the calculated slope is multiplied by the following "flow" calculation-constant to provide a final representative number for ice flow between adjacent elevation points, which essentially multiplies the "flowParam" constant by the average elevation between adjacent elevation, and divides the product by the subPlaneWidth:
        * flowParam * (elevations[i]+elevations[i+1])/2/subPlaneWidth
* a second for-loop iterates through each item in the "elevations" list:
    * each elevation item (except for the first and last items, which represent zero-elevation water centers) is calculated by taking any previous elevation item-value, and adding a new elevation value on top of it
    * new elevation values are created by multipling the "timeStepLength" variable by the "snowFall" variable, and then adding and subtracting flow values that are adjacent to each elevation point to calculate the ice that leaves and enters each elevation point; whatever value is created from this set of calculations is added to the previous elevation value
    * *although "snowFall" is constant among elevation centers, elevation differences arise initially due to elevation differences between the simulated plane and the simulated water at the edges of the graph (snow does not fall on water in this simulation)*
* after these two for-loops, the current year in the simulation is calculated, printed, and tested to see if it equals the total years that the simulation is set to run for
    * if the current year equals the total year, the overall graph-iteration for-loop breaks
    * if not, the overall graph-iteration for-loop continues; the axes clears its values, and the next iteration of the graph is set up with the same commands that set up the initial graph (with the addition of a plt.pause() function that pauses briefly between each new iterations)

**The final few commands of the program**

* the final year of the simulation is printed, along with a message showing the iterations have completed; plus, a final statistic showing the highest elevation point of the simulation

Have fun using the program!

