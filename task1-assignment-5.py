#creation of dictionary named details and keys as the name and marks as the value
details={"Ganesh":50,"Vignesh":45,"Ramesh":50,"Digvesh":15,"Shana":36}
search=input("enter the name of the student:")
a=search in details
if(a==True):
  z=details[search]
  print(search," found!")
  print(search,"\'s marks is: ",z)
else:
  print(search,"data doest not exist in our record")
