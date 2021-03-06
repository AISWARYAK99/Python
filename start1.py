#python beginning
'''
There are 6 data types in python.
1.Numeric(not mutable)
2.List(mutable)
3.Tuples
4.Dictionary
5.Set
6.String
'''
print('hello users welcome to the basics')
a=int(input('Enter num a:'))#input is read as a string so converting it to int.
b=int(input('Enter num s:'))#type conversion of string to int
print('The addition of a and is:',(a+b))

#data types

a=10
b=30
a=9
print(a)

#numeric dataype

a=10  #integer
b=-10
c=3.14 #Float
d=0.142
e=10+3j #Complex-numbers
f=6j
print(a+b,c-d,e-f,end='\n')
print(a-c,b-f,a*b,end='\n')

#type-conversions

s='10010' #String
c=(int)(s,2) # passing 2 since its a binary num we need to convert s to an integer of base 2 which is binary
print('After converting to integer base 2: %d ' %c,end='\n')

e=float(s)
print('After converting to float: %f ' %e,end='\n')

s='4' #initialising integer
c=ord(s) # char converted to integer
print('After converting character to integer : %d ' %c,end='\n')

c=hex(56)
print('After converting 56 to hexadecimal string : '  +c,end='\n')

c=oct(56)
print('After converting 56 to octal string : '+c,end='\n')

s='Aiswarya' #initialising string
c=tuple(s)
print('After converting string to tuple ',c,end='\n')

c=set(s)
print('After converting string to set ',c,end='\n')

c=list(s)
print('After converting string to list ',c,end='\n')

a=1
b=2
tup=(('a',1),('f',2),('g',3)) #initialising tuple

c=complex(1,2)
print('After converting integer to complex numbers ',c,end='\n')

c=str(a)
print('After converting integer to string ',c,end='\n')

c=dict(tup)
print('After converting tuple to dictionary ',c,end='\n')





