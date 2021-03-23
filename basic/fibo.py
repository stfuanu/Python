number = input("Enter the Range : ")
number = int(number)
a = 0
b = 1
      
for i in range(0, number):
           if(i <= 1):
                      x = i
           else:
                      x = a + b
                      a = b
                      b = x
           print(x)
