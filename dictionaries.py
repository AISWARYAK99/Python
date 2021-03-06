#Dictionaries
#it is mutable .It hold key value pair.
my_dict={}
my_dict1=dict()
print(my_dict)
print(my_dict1)

my_dict2={1:'Python',2:'Java'}
my_dict3=dict({1:'HTML',2:'C#'})
print(my_dict2)
print(my_dict3)

#accessing elements 
my_dict4={'First':'Pycharm','Second':'Spyder'}
print(my_dict4['First'])#get values by passing keys
print(my_dict4.get('Second'))

#adding and changing elements in a dictionary
print(my_dict4)
my_dict4['Second']='Vscode'
print(my_dict4)
my_dict4['Third']='Ruby'#adding elements
print(my_dict4)

#deleting elements
a=my_dict4.pop('Third')#remove this from the dictionary and returns the value at the passed key
print('Value at Third',a)
print(my_dict4)
b=my_dict4.popitem()#remove a keyvalue pair at random and returns them ad tuple
print('Key Value pair ',b)
print(my_dict4)
my_dict4.clear()
print(my_dict4)

my_dict5={1:'Aiswarya',2:'Archana',3:'Meera'}
print(my_dict5.keys())
print(my_dict5.values())
print(my_dict5.items())
print(my_dict5.get(1))
