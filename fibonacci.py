#Program to display the fibonacci sequence up to the n-th term 

def fibo(n):
  if n<=1:
    return n
  else:
    return (fibo(n-1)+fibo(n-2))

nterms=5

#check if the number is valid or not 

if(nterms<=0):
  print("Please enter a positive number")
else:
  print("Fibonacci sequece is :")
  for i in range(nterms):
    print(fibo(i))
