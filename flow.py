'''
a=10
b=15
if a==b:
    print('They are equals')
elif a>b:
    print('a is larger')
else :
    print('b is larger')

#nested if else stmnts

n=int(input('Enter a number'))
if n>=0:
    if n==0:
        print('Number is Zero')
    else:
        print('Number is positive'
else :
    print('Number is negative')

basket=['apple','orange','grapes','banana']
for i in basket:
    print(i)

numbers=[1,2,3,4,5]
sum=0
for i in numbers:
    sum+=i
print(sum)

for i in range(10):
    print(i)
print('\n')
for i in range(2,7):
    print(i)
print('\n')
for i in range(1,20,2):
    print(i)


#for else 
cakes=['pineapple','blueberry','strawberry']
for cake in cakes:
    print(cake)
else:
    print('No more cakes')

#while loop
second=10
while second>=0 :
    print(second,end='->')
    second-=1
print('Blastoff')

counter=0
while counter<3:
    print('Hello')
    counter+=1
else:
    print('No reply')
'''
#nested loop
count=1
for i in range(10):
    print(str(i)*i)
    for j in range(0,i):
        count+=1