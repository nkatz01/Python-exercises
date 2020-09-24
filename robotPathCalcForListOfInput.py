from numpy import sqrt
import numpy as np
from numpy import round
print()
lengthOfRoad_x=float(100)
secondSideOfRightTraiangle_y=float(20)
lengthOfRoadRobotTravels_r=np.array([80,82,84,86,88,90])
#meters per second
speedOfRoad_u=float(5)
speedOfTarrain_v=float(3)
timeOfTravelRoad_2=lengthOfRoadRobotTravels_r/speedOfRoad_u
# Calculating the Hypotenues
timeOfTravelTarrain_2=sqrt((lengthOfRoad_x-lengthOfRoadRobotTravels_r)**2+secondSideOfRightTraiangle_y**2)/speedOfTarrain_v
totalTravelTime_2=timeOfTravelTarrain_2+timeOfTravelRoad_2
print("For Road Length [80,82,84,86,88,90], travel time will be", round(totalTravelTime_2,1), 'Hr',)

