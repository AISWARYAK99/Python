#List data type
#lists are same as array but it could hold different data types in them.

my_list=[] #initialising empty list
print(my_list)

my_list2=list()#initialising empty list
print(my_list2)

my_list3=[1,2,3,'me','hey']
print(my_list3)

my_list4=list([4 , 5 , 3.356,'hey','que'])
print(my_list4)
print(my_list4[:])
print(my_list4[4])
print(my_list4[0:4])#0 to 3 gets printed
print(my_list4[::-1])#accessing elements in reverse order
print(my_list4[0:5:2])#0 to 4 will be printed with jumping of 2 elements instead of 1
print(my_list4[3][2])#prints 3rd index elements 2 indexed element

#adding elements to the last of list
my_list4.append(['Ais',12])#adds it as a single element
print(my_list4)
print(len(my_list4))#returns length of the list

my_list4.extend(['Ais',12])# adds elements one by one
print(my_list4)
print(len(my_list4))

my_list4.insert(1,'Lets_go')
print(my_list4)

print(my_list4 +['trial'])#concatenation
print(my_list4 * 2)#multiply
print(my_list4)

#deleting elements from list
del my_list4[5]
print(my_list4)

my_list4.remove('Ais')#delete the passed element if present else error
print(my_list4)

a=my_list4.pop(5)# returns the deleted element
print('poped element is ',a,' remaining list ',my_list4)

my_list4.clear()
print(my_list4)

#Other functions
my_list5=[4,5,3.142,'fun','cool']
new=[1,77,8,5,9.00]
print(len(my_list5))
print(my_list5.index('cool'))
print(my_list5.count('fun'))# num of times fun occurs in the list
print(sorted(new))#sorts elements in the list but doesnt change the original
print(new)

new.sort(reverse=True)#sorts original list in descending order if reverse=True else in ascending order
print(new)

new.reverse()#reverse list elements
print(new)

new_list=my_list5.copy()
print(new_list)



