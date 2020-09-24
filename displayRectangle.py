#nuchem katz 10.12.2017
#This programme uses  a single for loop to display
#a rectangle of asterisks with a given height and a given width

length=input("Enter length of rectangel (counted in asterisks) : ")
hight=input("Enter hight of rectangel  (counted in asterisks) : ")
l=int(length)
h=int(hight)
print("* "*l)
for h in range(h-2):
    print("%s%s%s"%("*"," "*((l*2)-3),"*"))#Subtracts 2 spaces for the
#astricks and one space for the space followed the lengths of the top and the bottom
print("* "*l)