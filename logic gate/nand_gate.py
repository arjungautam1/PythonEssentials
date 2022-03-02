# Program to implement NAND gate using python 

def AND(A,B):
  return A&B

def NOT(A):
  return ~A+2

def NAND(A,B):
  return NOT(AND(A,B))

print("Output of 0 NAND 0 is",NAND(0,0))
print("Output of 0 NAND 1 is",NAND(0,1))
print("Output of 1 NAND 0 is",NAND(1,0))
print("Output of 1 NAND 1 is",NAND(1,1))