#!/usr/bin/Python 

# billiescodes 2016
# Exercise #3 : List less than ten
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# take a list --> write a program that prints out all the elements less than 5
	#1. make new list print out entire list
	#2. write this in one line of python 
	#3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user

def nulist(list,num):
	nu = []
	for i in range(len(list)): 
		if list[i] < num: nu.append(list[i])
	print nu



def main():

	print " \n\t\t\t ~ List less than Ten Program ~ \n " 
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

	### remember: For loops :
		# For a in list:						--> to go over each element
		# For a in range(len(list)) --> to go over each index 
	print " \t Part 1: "
	for i in range(len(a)) : 
		if a[i] < 5: print a[i]

	### Part 2: function nulist(list)
	print " \n\t Part 2: " 
	nulist(a,5)

	### part 3:
	print " \n\t Part 3: code in one line, best so far: 2 lines" 
	# 2 lines of code, can't figure out in one :( 
	for var in a:
		 if var < 5: print var	

	### part 4:
	print "\n\t Part 4: please input a benchmark number... "
	prompt = '>'
	inpt = int(raw_input(prompt))
	print " all the numbers lower than {0} are".format(inpt) 
	nulist(a,inpt)

# Boilerplate end of the file stuff
if __name__ == '__main__':
	main()	


