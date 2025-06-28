f=open("output.txt",'w')#write mode and file opening
c=f.write("\nI am ######## your py tutor")#writing data into the file
print(c)
f.close()#closing of file
chat=str(input("enter a data to be entered in the file:"))#input from  user
f=open("output.txt",'a')#opening the file in append mode
new=f.write(chat)#input from user is added to the file without deleting the previous data
print(new)
f.close()#closing of file
f=open("output.txt",'r')#file opening in read mode
ch=f.read()#data from file is extracted to the ch string
print(ch)#ch string is printed
f.close()#file is closed
