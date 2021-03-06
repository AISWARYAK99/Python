#pass by objects
def foo(bar):
    bar='new value'
    print(bar)
answer='old value'
foo(answer)
print(answer)

def add(a,b):
    print('Sum is',a+b)
def multiply(a,b):
    print('Product is',a*b)

add(5,10)
add(9,6)
multiply(6,1)

#in built functions

list=[1,0,3]
print(abs(-7))#return positive value of the passed argument
print(all(list))#returns true if all elements are true
print(any(list))#returns true if any one element are true
print(min(list))
print(max(list))
print(len(list))
print(sum(list))
print(type(list))