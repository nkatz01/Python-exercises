#program that takes input integer by integer and prints out the maximum inputed as well as its position in the sequence.

maxi=0.0
total=0.0
ind=-1
pos=1
inputStr=input("Enter value")
while inputStr!="":
  ind=ind+1
  value=float(inputStr)
  if maxi<value:
    maxi=value
    pos=ind+1
  inputStr=input("Enter value :")
print(maxi)
print(pos)
