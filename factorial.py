#Python program to find the factorial of number provided by ther user 

def factorial(x):

  if x<=1:
    return 1
  else:
    return (x*factorial(x-1))


num=int(input("Enter any number :"))
result=factorial(num)
print("The factorial of number is : ",result)