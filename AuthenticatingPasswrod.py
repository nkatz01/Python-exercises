password=input("Please enter your password (should contain atleast one upper case, lower case, one digit and charecter")


if password.isalpha():
  print('Your password only contains letters')
  if password.isupper():
    print('Your password contains only upper case letters')
  elif password.islower():
    print('Your password contains only lower case letters')
  elif 'A'<=password[0]<='Z':
    print('Your password begins with an upper case letter')
elif password.isdigit():
  print('Your password only contains digits')
elif password.isalnum():
  print('Your password contains only letters and digits')
elif password.endswith('.'):
  print('Your password ends with a period')
elif 'A'<=password[0]<='Z':
  print('Your password begins with an upper case letter')
else:
  print('Your choice of password is accapted')