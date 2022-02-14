# Welcome to my Ice Sheet Simulator

This is a program based on the "Simple I-D Ice Sheet Flow Model" that is a part of the "Global Warming II: Create You Own Models in Python" Coursera course, provided by the University of Chicago.

This main output of this program is a moving pseudo-bell curve graph that simulates the elevation-growth of a sheet of ice on a 1,000,000 meter-wide (1-dimensional) flat plane. 

The simulated ground is flanked by two patches of water (not unlike a larger landmass like Greenland), and it gains its ice from 0.5 of "snowfall" per year. As the ice accrues in the simulation, an "ice hill" develops based on continous snowfall raising the elevation of settled ice, and ice slowly "flows" downhill into the surrounding water (as dictated by a flow constant, etc.).

The main point of this program is to give a sped-up and simplified visual of the specific way that ice accrues, and flows down itself.

## What the program does, in simple terms

**Setting up variables to represent elevation points, and plane dimensions (for the purposes of future calculations):**
* ten "elevation points" are set up with the "nElevationCenters" variable, to set the number of changing elevation points needed for the simulation 
* the total width of the flat ground/plane that the snow will fall on (1,000,000 meters) is defined with the "totalPlaneWidth"
* this flat plane is divided by the "nElevationCenters" variable to divide the plane into ten equal widths (one part for each "elevations point"), and the resulting number is stored in the "subPlaneWidth" variable. 

**Setting up variables to represent time iterations (for the purposes of future calculations):**
* the simulation displays itself visually by constantly resetting values in graph-form, like a flip-book;e ach new iteration of the graph simulates a time step
* the length of each time-step is defined by the "timeStepLength" variable, which is set to "100 (years)" 
* the total number of years that the simulation will run for is set by the "totalYears" variable; this is set to "15000 (years)", mostly because this is where the simulation "levels" out based on all of the other inputs
* the number of time-steps taken is calculated by dividing "totalYears" by "timeStepLength"

**Setting up variables to represent snow/ice movement (for the purposes of future calculations):**
* the "snowFall" variable holds a number representing meters of simulated snow that falls each year (0.5 meters) 
* the "flowParam" is a holds a "flow constant" number (10,000) that governs and accounts for "horizonal" ice-flow "downhill" between elevation points; this is a constant provided by the original course instructor that gives more nuance to "flow calculations" later in the program to better simulate the flow of ice.

**Setting up lists to hold elevation and flow values (for the purposes of future calculations):**
* two lists of multiple zeros are calculated: an "elevations" list (that we will use to collect and plot elevations values), and a "flows" list (that we will use to collect flow values, and use them to iteratively change "elevations items")
* the number of items in the "elevations" list is equal to "nElevationCenters+2" so that we have "elevations" items for each "elevation center", as well as an extra 2 to represent "water" points (that will always have zero elevation) that flank the "elevations" values
* the number of items in the "flows" list is equal to "nElevationCenters+1" so that we have "flow" items that exist "in between "elevations points" (or between an "elevation point" and "water point" where applicable)
* the zeros in these lists are placeholders for future values
* *a visual of "where" flows points are "located" in relation to elevation/water points can be seen as comments after these list initializations* 


Have fun using the program!

