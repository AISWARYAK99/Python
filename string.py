#strings
#collection of characters. it is not mutable.

my_str='Strings Introduction'
my_str1='This is a String'
print(my_str)
print(my_str1)

#string splicing
print(my_str[:])#prints entire string
print(my_str[2:10])#prints from index 2 to 9
print(my_str[0:14:1])#prints from index 0 to 13 jumping 1 element
print(my_str[0:14:2])#prints from index 0 to 13 jumping 2 element
print(my_str[::-1])#reverses strings
print(my_str[-7:-1])

#other functions
print(my_str.count('s'))#num of times s is there in that string
print(len(my_str))#returns len of string
print(my_str.lower())#converts entire string to lower case
print(my_str.upper())#converts entire string to upper case
print(my_str.find('t'))#returns the index where t first comes in the string if not found then error
print(my_str.partition('tro'))#breaks string into tuple for the element passed
print(my_str.split(' '))#split string for the parameter passed and returns in a list
print(my_str.replace('Strings','This is an'))#replace Strings with the passed one