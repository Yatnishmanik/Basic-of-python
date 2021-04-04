# range 
x=range(10)
print(x[0])
print(x[1])
print(x[2])
print('*********')
y=range(1,10)
print(y[0])
print(y[1])
print(y[2])
print('*********')
z=range(1,10,2)
print(z[0])
print(z[1])
print(z[2])
print('*********')

# range use in For Loop
for i in x:
    print(i)
print('second loop')
x=range(1,10,2)
for i in x:
    print(i)

print('*********')
# For Loop
x='yatnish'
n=len(x)
for i in range(n):
    print(i,'=', x[i])
    
