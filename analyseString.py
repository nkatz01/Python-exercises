#Nuchem Katz 11.12.2017
#This program gete the first character of a string, The last character
#The middle character (if the length is odd),)
#The middle two characters (if the length is even
string=input("Enter string : ")
print(string[0],string[-1])
if len(string)%2==0:
        midleftpointer=int(len(string)/2)-1
        midrightpointer=int(len(string)/2)
        print(midleftpointer)
        print(midrightpointer)
        print(string[int(len(string)/2)-1],string[int(len(string)/2)])
else:
        print(string[int(len(string)/2)])
