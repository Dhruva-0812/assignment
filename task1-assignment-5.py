#creation of dictionary named details and keys as the name and marks as the value
details={"GANESH":50,"VIGNESH":45,"RAMESH":50,"DIGVESH":15,"SHANA":36}
search=input("enter the name of the student(all in uppercase):")
a=search in details
if(a==True):
  z=details[search]
  print(search," found!")
  print(search,"\'s marks is: ",z)
else:
  print(search,"data doest not exist in our record")
