
print()
r=2.0
n=2.0
b=2.0
c=b*1+r/100**n
print(c)
print(b*1+r/100**n)
print(b*(1+r/100)**n)
#calculate cost of a car by calculating the distance driven
#/by fuel efficiency * miles driven * fuel cost * years of operation
# + cost of purches.
purchesPrice=10000
numberOfYears=10
annualMilesDreiven=15000
fuelEfficiency=20
pricePerGallon=4.00
annualFuelConsumed=annualMilesDreiven/fuelEfficiency
annualFuelCost=pricePerGallon*annualFuelConsumed
operatingCost=numberOfYears*annualFuelCost
totalCost=purchesPrice+operatingCost
print("Total cost is of the car is", totalCost)


print()
#Nuchem Katz 17-10-2017
x=2
y=3
print("The sum of the two integers is 8")
#The sum 
print(y+x)
#The difference
print(x-y)
#The product 
print(x*y)
#The average
print((y+x)/(y+x))
#The absolute value of the difference
print((-x)-(-y))
#or
print(abs(x-y))
#The maximum
print(abs(y+x))
#or does it meant this? 
print(max(y,x))
print(min(y,x))
