password=input("Please enter a password of atleast 8 characters, containing one digit, upper and lower case letter")
digit=False
uper=False
lower=False
passed=False
if (len(password)>=8):
    for i in password:
      if i.isdigit()==True:
        digit=True
      elif i.isupper()==True:
        uper=True
      elif i.islower()==True:
        lower=True
passed=(uper and lower and digit)==True
if uper==False and lower==False and digit==False:
  print('password not long enough')
else:
  if digit==False:
    print("Password's missing a digit")
  if uper==False:
    print("Password's missing an upper case letter")
  if lower==False:
    print("Password's missing a lower case letter")
