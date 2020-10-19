#nuchem katz 12.1.2018
#this program swaps two given letters in a word. 
word=input("Enter a word in which you'd like to swap around two charachters (eg, all the e's with all the a's : ")
letterToBeSwapped=input("Enter the characters you'd like to swap starting with character one : ")
letterSwappedWith=input("Now, please enter the second character : ")
letter1found=False
letter2found=False
for letter in word:
  if letter==letterToBeSwapped:
    letter1found=True
  elif letter==letterSwappedWith:
    letter2found=True
if letter1found and letter2found:
  asterisc="*"
  word=word.replace(letterToBeSwapped, asterisc)
  word=word.replace(letterSwappedWith, letterToBeSwapped)
  word=word.replace(asterisc,letterSwappedWith)
  print(word)
else:
  print("I'm sorry one of the characters you entered is not found in your chosen word - pls try again. Good bye!")

