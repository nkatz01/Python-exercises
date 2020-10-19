from random import randint
word=input('Enter a word in which you want two random letters permuated')
for times in range(len(word)):
 i=randint(0,len(word)-2)
 j=randint((i+1),len(word)-1)
 string_i=word[i]
 string_j=word[j]
 first=word[0:i]
 middle=word[(i+1):j]
 last=word[(j+1):len(word)]

print(first+string_j+middle+string_i+last)