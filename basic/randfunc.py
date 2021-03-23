import random
import re
import subprocess

def gurl( ):
	my_file = open('comm101.txt')
	all_the_lines = my_file.readlines()
	ount=len(all_the_lines) # No. of files
	#rand=random.randint(0,(ount-1))
	filename="out.txt"
	#rand=random.randint(0,(ount-1))
	#with open(filename, 'a') as file_object:
	#	file_object.write(str(rand)+" ")
	l = open('out.txt').read().split()
	l2=(set(l))
	l3=list(l2)
	print(l3)
	#print(l2)
	#################################################################

	while (8>5):
		rand=random.randint(0,(ount-1))
		#print("while try : "+str(rand))
			#print("inside with")
		if str(rand) not in l3 :
			print("New Rand :"+str(rand))
			with open(filename, 'a') as file_object:
				file_object.write(str(rand)+" ")
			break
		else:
			continue



	#subprocess.call("cat out.txt")
	url=all_the_lines[rand]
	#print(rand)
	print(url)
	#print("SPACE")





a=[1,2,3,4,5]
for x in a:
	one_next =gurl( )
