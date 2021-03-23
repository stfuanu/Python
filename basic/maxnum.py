a = input("Enter First Number : ")
b = input("Enter Second Number : ")
c = input("Enter Third Number : ")

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
	print("\nNumbers : "+a+" , "+b+" & "+c+" !!")
	print("\nBiggest Number out all three is :",c)
