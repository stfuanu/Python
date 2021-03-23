file = input("Enter FileName : ")
deli = input("Enter Delimeter : ")
choi = input("Do you want to save the splited result ? : ")

#print(file)
liist = open(file).read().split( deli )
for x in liist:
	print(x)

filename = 'comm.txt'

if choi == 'y':
	dest = input("Enter Destination FileName : ")
	for z in liist:
		with open(dest, 'a') as destination: # comm.txt is API FILE
			destination.write(z+"\n")
elif choi == 'n':
	False
else :
	False
