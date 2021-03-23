
num = input("Enter a number: ")
num = int(num)

x = 1

if num < 0:
   print("Factorial doesn't exist for -ve numbers")

elif num == 0:
   print("Factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       x = x*i
   print("Factorial of",num,"is",x)