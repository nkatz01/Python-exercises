#nuchem katz 11.12.2017
#this program prompts user to input a non-empty list of strictly positive integers from the keyboard.
#The end of the input is indicated by 0.
#The program then prints out the following numbers.
#The average
#The smallest of the values
#The largest of the values
#The range
number=input('Enter first integer or press 0 to terminate')
while (int(number))<0:#does not allow for negative
    number=input('integer has to be above 0. Pls try again')
total=int(number)
firstInt=total#is recording first value of integer in list
count=1#is going to count inputs to later calculate avarage
highest=int(number)
lowest=int(number)
if number!='0':
    while number!='0':
        number=input('Enter next integer or press 0 to terminate list')
        if int(number)!=firstInt or count>1:#second integer must be different than first
            newnumber=int(number)
            if newnumber>0:#again, is not allowing for negatives
                count=count+1
                total=total+newnumber
                if newnumber>highest:
                    highest=newnumber
                elif newnumber<lowest:
                    lowest=newnumber
            elif newnumber<0:
                print('integer has to be above 0. Pls try again')
        else:
            print('at least one integer must be different integer. Pls try again')
    print("You've indicated that you finished your input and are ready for results.")
    avarage=total/count
    _incRange=(highest-lowest)+1
    print("Results: The avarage =",avarage, "highest =",highest,
          "lowest =",lowest,"inclusive range =",_incRange)
else:#is communicating with user that it hadn't entered the while at all
    print("You've ordered the program to terminate. 'Good bye'")

