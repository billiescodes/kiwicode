#!/usr/bin/Python

#billiescodes 2016

# Exercise 13; 13_Fibonacci.py

#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# without main function

def fibo(num):

	flist=[1,1]
	if num < 3:
		print "boo"
		if num==1: return flist[0]
		if num==2: return flist[:2]
	else:
		for a in range(2,num):
			print "crap"
			print flist
			flist.append(flist[a-1]+flist[a-2])	
		
		return flist


inpt=int(raw_input("please enter the number of Fibonacci numbers to print, and don't be a dick, enter an integer: \n", ))
	
	
fin_list = fibo(inpt)
print " the {} numbers of the Fibonacci sequence: \n {}".format(inpt, fin_list)


 
