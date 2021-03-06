#operators are constructs used to manipulate data
#Arithmetic Operators
a=10
b=5
print('Addition',a+b)
print('Subtraction',a-b)
print('Multiplication',a*b)
print('Division',a/b)
print('Remainder',a%b)
print('Exponential',a**b)

#Assignment Operators
add,sub,mul,div,rem,exp=0,0,0,1,1,1
add+=a #add=add+a
print(add)

sub-=a
print(sub)

mul*=a
print(mul)

div/=a
print(div)

rem%=a#rem=rem%a
print(rem)

exp**=a
print(exp)

#comparison operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical operators
c=5
d=0
print(c and d)
print(c or d)
print(not c)
print(not d)

#Bitwise operators
e=5
f=6
print(e & f)#bit by bit and operation
print(e|f)#bit by bit or operation
print(e^f)#bit by bit xor operation
print(~e)#complement
print(e<<f)#left shift operation.shifting by 1 equivalent to multiplying by 2(that is 5*2 6 times =320)
print(e>>f)#right shift operation.shifting by 1 equivalent to diving by 2

#Identity Operators
g=[1,2,3]
h=[2,3,4]
print(g is h)
print(g is not h)

#Membership Operators
x=[1,2,3]
print(2 in x)
print(2 not in x)