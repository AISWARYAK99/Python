#sets
#unordered coollection of unique elements.it is mutable
my_set={1,2,3,4,5,5,5}#5 will be printed only 1 time since set allows only unique elements
print(my_set)

#adding elements
my_set1={1,2,3}
my_set1.add(4)
print(my_set1)

#other methods
my_set2={1,2,3,4}
my_set3={3,4,5,6}
print(my_set2.union(my_set3),'---->',my_set2|my_set3)
print(my_set2.intersection(my_set3),'------>',my_set2 & my_set3)
print(my_set2.symmetric_difference(my_set3),'------->',my_set2^my_set3)
print(my_set2.difference(my_set3),'------>',my_set2-my_set3)
my_set2.clear()
print(my_set2)

#operators in sets
superset={1,2,3,4,5,6,7,8,9,10}
s1={1,2,3,4}
s2={3,4,5,6}
print(s1 == s2) #if symmetric
print(s1!=s2) #if not symmetric
print(s1<=superset) #if s1 is a subset of superset
print(s1<superset) ##if s1 is a proper subset of superset
print(s1>=s2) # if  s2 is a subset of s1
print(s1>s2) # if s2 is a subset of s1
