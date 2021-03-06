#tuples
#they are not mutable
my_tuple=()
my_tuple1=tuple()
print(my_tuple)
print(my_tuple1)
my_tuple=my_tuple+(1,2,3)
print(my_tuple)

my_tuple2=(1,2,3)
my_tupple4=tuple(('Python','Java','Php',1))
print(my_tuple2)
print(my_tupple4)
my_tuple5='example', #add comma if we want tuple with single elements
print(type(my_tuple5))

#Accessing elements
my_tuple6=(1,2,3,['Hindi','telugu'])
print(my_tuple6[0])
print(my_tuple6[:])
print(my_tuple6[3][1])#2 element of 3rd index
print(my_tuple6[::-1])#accessing elements in reverse order
print(my_tuple6[0:5:2])#0 to 4 will be printed with jumping of 2 elements instead of 1

my_tuple6[3][1]='English' #we can change values of a tuple since it is immutable but we since the 3rd index of tuple is a list we can change the list component of that tuple.
print(my_tuple6)

#tuple methods
my_tuple7=(1,2,3,'English')
print(my_tuple7.count('English'))
print(my_tuple7.index('English'))
