# control statements "if"
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
if(x==y):
    print('value is equal')
print('rest program execute')

# control statements "nested if"

x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
z=int(input('enter the value of z:'))
if(x==y):
    print('value is equal x and y')
    if(x==z):
        print('all values are equal')
print('rest program execute')
# control statements "if else "
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
if(x==y):
    print('value is equal')
else:
    print('value is not equal')
print('rest program')
# control statements " nested if else "
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
if(x!=y):
    print('hi')
    if(x==100):
        print('Hi')
    else:
        print('bye')
else:
    print('dont disturb')
print('rest program')
# control statements " if elif "
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
if(x==y):
    print('equal')
elif(x<y):
    print('lesser')
elif(x>y):
    print('greater')
print('rest program')
# control statements " if elif else "
x=int(input('enter the value of x:'))
if(x==1):
    print('x is one')
elif(x==2):
    print('x is two')
elif(x==3):
    print('x is three')
elif(x==4):
    print('x is four')
else:
    print('value is greater then 4')
print('rest program')
