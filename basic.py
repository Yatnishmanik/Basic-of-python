# for knowing address of any variable
x=23
print("value of x=",x)
print(id(x))

print(" airthmatic operation")
print(2*3)
print(2/5)
print(2+3)
print(3-2)
print(3**2)#for exponenet 3 to power 2
print(3//2)#for round off
print(3%2)#for reminder

print(" relation or comparison  operation")
print(3<5)
print(3>5)
print(3<=3)
print(5==5)
print(5!=3)

print(" logical operation")
print((3<5)and(4<5))
print((3<5)or(4<5))
print(not(4<5))
z="yatnish manik"
print((5<6)and(z))
print((5>6)and(z))

print(" assignment operation")
#1
x=3
x+=1
print(x)
#2
x=4
x-=3
print(x)
#3
x=5
x%=5
print(x)

print(" bitwise operation")
x=10
y=19 # here 10 and 20 is first  coverted into binary then apply "and" truth table
z=x&y
print(z)
r=x|y
print(r)
v=x^y # '^'for XOR gate
print(v)
k=x<<2 # '<<'for bitwise left shift
print(k)
l=x>>2# '>>' for bitwise right shift 
print(l)

print(" membership operation")
str="yatnish manik is conqure"
print('yatnish'in str)
print('is' not in str)

print("identity operation")
str='always cool'
print('cool' is  str)
print('cool' is not  str)


