#nuchem katz 12/12/2017
#no parameters
#returns a the inputed string if it is above 0 or an empty string if it is below 0
def getIntegerString():
    numString=input('Please enter an integr greater than or equal to 0 : ')
    numInteger=int(numString)
    if numInteger<0:
        return "><"
    else:
        return numString
print(getIntegerString())
print(getIntegerString())
#param a string of caracters
#retruns the string reversed 
def reverse(myString):
    _reversed=""
    letter=(len(myString)-1)
    while letter>=0:
        _reversed=_reversed+myString[letter]
        letter=letter-1
    return _reversed
print(reverse('123450'))
#@param a string of caracter
#@returns the string concatenated with the reverse of that string
def mirror(myString):
    _chopped=""
    count=0
    while count<(len(myString)-1):
        _chopped=_chopped+myString[count]
        count=count+1
    return _chopped+reverse(myString)
print(mirror('12345'))



def main():
  intString=(getIntegerString())
  newIntString=(mirror(intString))
  if int(newIntString)%2==0:
    return"The number", intString, "reversed and concatenated comes to an evnen number", newIntString
  else:
    return"The number", intString, "reversed and concatenated comes to an odd number", newIntString
       
print(main())
print(main())