from math import sqrt
lengthOf1stRoadSegment=float(input("Enter length of road in meters"))

#The programe will now ask for the second segment of Road which we want the robot, to cut
bottomSideOfRightTrangle=float(input("Enter second segment of Road in meters (i.e. adjacent side of the triangle:2"))
secondSideOfRightTraiangle=float(input("Enter the opposite side of the   triangle"))

speedOfRoad=float(input("Enter speed of robot on the road in km/h"))
speedOfTarrain=float(input("Enter speed of robot on tarrain in km/h"))
timeOfTravelRoad=lengthOf1stRoadSegment/speedOfRoad

# Calculating the Hypotenues
lengthOfTarrain=sqrt(bottomSideOfRightTrangle**2+secondSideOfRightTraiangle**2)
timeOfTravelTarrain=lengthOfTarrain/speedOfTarrain
totalTravelTime=timeOfTravelTarrain+timeOfTravelRoad

print("Total time of Travel is", round(totalTravelTime,1),"hours",)
