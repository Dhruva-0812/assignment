def factorial(a):
  if(a<2):
    return 1
  else:
    return a* (factorial(a-1))
z=int(input("enter a number for its factorial:"))
result=factorial(z)
print("factorial of ",z," =" ,result)
