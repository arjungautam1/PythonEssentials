# Program to implement NOR using python 

def OR(A,B):
  return A | B

def NOT(A):
  return ~A+2

def NOR(A,B):
  return NOT(OR(A,B))

print("Output of 0 NOR 0 is",NOR(0,0))
print("Output of 0 NOR 1 is",NOR(0,1))
print("Output of 1 NOR 0 is",NOR(1,0))
print("Output of 1 NOR 1 is",NOR(1,1))