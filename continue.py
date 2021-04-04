# continue statements
x=int(input('enter the value of x'))
for i in range(x):
    if(i<=2):
        continue # here continue send the contol to the for loop (for values0,1,2)no other part execute in For-loop 
    else:
        print('block')
        i+=1    
    print(i)
# pass statement

x=int(input('enter the value of x'))
for i in range(x):
    if(i<2):
        pass # here if cond' satisfy then no else part execute only rest part executein loop 
    else:
        print('racer')
    print('rest part ')
# assert statement
x=int(input('enter the value of x greater 5'))
assert x>5,'not under 5'
print(x)
