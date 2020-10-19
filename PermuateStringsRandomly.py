from random import randint
word=list(input('Enter a word in which you want two random letters permuated'))
for times in range(len(word)):
 i=randint(0,len(word)-1)
 j=randint(0,len(word)-1)
string_i=word[i]
word[i]=word[j]
word[j]=string_i
print("".join(word))