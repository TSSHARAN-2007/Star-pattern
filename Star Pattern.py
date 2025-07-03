# Triangular star matrix:
n = int(input(("Enter the dimension of star matrix: ")))
if n<=1:
   print("Value is not cooperative.")
for i in range(1,n+1):
      spaces = n-i
      stars = i
      print(" "*spaces+"*"*stars)