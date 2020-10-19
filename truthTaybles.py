#Nuchem Katz 07.11.2017
a=int(input("Enter the first value"))
b=int(input("Enter the first value"))
c=int(input("Enter the first value"))
p=(a!=0)
q=(a!=0)
r=(a!=0)
print(p and q or (not r))

spaces='      '
print('p'+spaces+'q'+spaces+'r'+spaces+'(p and q or (not r)')
p=True
q=True
r=True
print(p,q,r, spaces, (p and q) or (not r))
p=False
q=True
r=True
print(p,q,r, spaces, (p and q) or (not r))
p=False
q=False
r=True
print(p,q,r, spaces, (p and q) or (not r))
p=False
q=False
r=False
print(p,q,r, spaces, (p and q) or (not r))
p=True
q=False
r=False
print(p,q,r, spaces, (p and q) or (not r))
p=False
q=True
r=False
print(p,q,r, spaces, (p and q) or (not r))
p=False
q=False
r=True
print(p,q,r, spaces, (p and q) or (not r))
p=True
q=False
r=True
print(p,q,r, spaces, (p and q) or (not r))

print()
#Nuchem Katz 07.11.2017
x=int(input("Enter the first integer"))
y=int(input("Enter the second integer"))
z=int(input("Enter the third integer"))
print((y==z and x!=y) or (y==x and z!=y) or (x==z and y!=x))
