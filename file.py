file1=open('dem.txt','w')#writes data to the file by deleting all previous data in that file if that file doesnt exist it will be created
for text in range(100):
    file1.write('Hey There!.\n')
file1.close()

file3=open('demo.txt','a')#appends data into the file without deleting the file contents
for text in range(2):
    file3.write('Hey There Again!.\n')
file3.close()

file2=open('demo.txt','r')
count=0
for lines in file2:
    count=count+1
print(count,'lines are present')
file2.close()