print()
print(1+2+3+4+5+6+7+8+9+10)

print("balance after 15 years: ",10000*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05*1.05)

print("If you add the first 10 positive integers to each other like that(1+2 1+3...+10) the total is", 11*5)

print("Similarly if you do this up to 1000 the total will be", 1001*500)




print()
# This program computes the volume (in litres) of a six-pack of soda
# cans and the total volume of a six-pack and a two-litre bottle.
#

# Litres in a 12-ounce can and a two-litre bottle.
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0
# Number of cans per pack.
cansPerPack = 6
# Number of two-litre bottles that are purchesed 
quantity = 2
# price of a single two-litre bottle of soda
unitPrice = 3
# Calculate total volume in the cans.
totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "litres.")
# Calculate total volume in the cans and a 2-litre bottle.
totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and a two-litre bottle contain", totalVolume, "litres.")
print("The price of a two-litre bottle is $3, thus a purches of 2 two-litre bottles of soda will come to $",unitPrice*quantity)	


print()
# This Program   calculates the square root of 2 by iteration. It starts of with x as the value half of 2 which is 1
# and by continuesly adding half of x (which we call 'delta') to x and then powering up x by itself. In the case of x being 1.5 after the first iteration, it keeps giving
# a lower and lower results closer to 2 but not less than 2. This is because everytime it redefines
#delta in an iteration it creates a small -float which is then added to x, therby making x smaller from 1.5 for eg. (in the second iteration)
# and so this is then multiplied by itself to check the newer proximity it has gotten to 2.
# And so it goes on getting all the time closer and closer but never quite getting exactly to it.
# Initialize x
x=1.0
print("x*x:", x*x)
# First iteration
delta = (1/x)-x/27
x = x+delta
print("x*x:" , x*x)
# Second iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)
# third iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)
# forth iteration
delta = (1/x)-x/2
x = x+delta
print("x*x:", x*x)
print("The square root of 2 is", x,)


print()
# This programme begins with an assignmnet of 1 to the vairable mystery,
# printing it in line 2
mystery = 1                # line 1
print(mystery)              # line 2
mystery = 1 - 2 * mystery  # line 3
mystery = mystery + 1      # line 4
# mystery is - 2 in line 3.
# It is then is again overriden in line 4, gaining 2, thus reaching 0. 
print(mystery)              # line 5

print()
print("_______")
print("|Nuchem|")
print("———————")

print()
print("*   * *   *  ***  *    * *****   **     **")
print("**  * *   * *     *    * *       * *   * *")
print("* * * *   * *     ****** ****    *  * *  *")
print("*   * *   * *     *    * *       *   *   *")
print("*   *  ***   ***  *    * *****   *       *")

print()
print("Mark Bool","     ","21.12.1990")
print("Phil Wine","     ","13.11.1985")

print()
l=10
w=7
h=5
numberOfDoors=2 
numberOfWindows=3
numberOfWalls=4
sizeOfDoors=1.5*3
SizeOfWindows=.5*1.75
areaNeededPaint=(l*w*h*numberOfWalls)-((sizeOfDoors*numberOfDoors)+(SizeOfWindows*numberOfWindows))
print("The Surface area to be painted is", round(areaNeededPaint,2), "Ft")

print()
purches=19.93
payment=20.00
change=payment-purches
print(payment, "-", purches, "=", round(change,2))

print()
word="mississippi"
print (word[:3],"...", word[-3:],)

print()
#inch to mm
const_inchINmm=25.4
letterSizeInInch1=8.5
letterSizeInInch2=11
letterDimension1=letterSizeInInch1 *const_inchINmm
letterDimension2=letterSizeInInch2*const_inchINmm 
print("Converting a letter whoes dimensions are", 8.5, "by", 11, " in inchs, to millimetre - will get you", round(letterDimension1,1), "by", letterDimension2, " in mm", )

print()
from math import sqrt
a=3 
b=4
area=a*b 
parimetre=(a*2)+(b*2)
diagonal= sqrt(a*a)+(b*b)
print("The diagonal of a rectangle with sides of length=",b, "and hight=",a, "has a parimetre of", parimetre, "and a diagonal of",diagonal,)

print()
gas=486#number of gallons of petrol
fe=1.46#gollon per mile - fule efficiency
priceOfGallon=3.75
distanceOnGas=gas/fe 
costPer100Mile=100*fe*priceOfGallon
print("A machine that contains", gas, "gallons of petrol, for the cost of", priceOfGallon, "a gallon, with a fuel efficiency of", fe, "per mile, will travel", round(distanceOnGas,1), "miles, for the cost of £%6.2f" %   round(priceOfGallon*gas,2),". 100 miles will cost him £%6.2f" %costPer100Mile,)

print()
#separate digits
firstd=16348//10000
secondd=16348//1000%10
thridd=16348//100%10 
forthd=16348//10%10
fifthd=16348%10
print(firstd,secondd,thridd,forthd,fifthd)
print()

print()
#This programm computes the total price of an order of books. Nuchem Katz 21.10.2017
totalBooksPrice=float(input("Please enter the total book price:"))
numberOfBooks=int(input("Enter the number of books you are purchesing:"))
tax=totalBooksPrice*(7.5/100)
shippingCharge= numberOfBooks*2.00
totalBookOrder=totalBooksPrice+tax+shippingCharge
print("Your total order amount is", round(totalBookOrder,2))


METERS_IN_A_MILE=1609.34
YARDS_IN_A_MILE=1760
FEET_IN_A_YARD=3
INCHES_IN_A_FOOT=12
meters=float(input("Please enter measurement in meteres:"))
miles=meters/METERS_IN_A_MILE
numberOfMiles=int(miles)
feet=(miles-numberOfMiles)*YARDS_IN_A_MILE*FEET_IN_A_YARD
numberOffeet=int(feet)
inches=(feet-numberOffeet)*INCHES_IN_A_FOOT
print("That is", numberOfMiles, "MIles", numberOffeet, "feet", "and", round(inches,2), "inches",)

