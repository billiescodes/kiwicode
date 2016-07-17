#!/usr/bin/Python

# billiescodes 2016
# Exercise 2: 2_odd-even.py
#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
	# 1. write the exercise in main
	# 2. write the modulus check as a function
	# 3. write multimodcheck function 
	# 4. NEW STYLE OF FORMATTING: use the .format method

def modcheck(num): 
	#check if multiple of 4:
	if num % 4 == 0: 
		print " number is even AND multiple of 4 !*** " 
		return	## place return statement here (not break) to exit function if you enter this part
	
	#check if odd/even
	rem = num % 2
	if rem == 0: print " number is even! \n" 
	elif rem ==1: print " number is odd! \n"


def multimodcheck(mod1,mod2):
	#check for this:  mod1 /mod2 = even
	rem = mod1%mod2  
	if rem ==0: print "{0} divides {1} evenly".format(mod2, mod1)				# use the FORMAT method
	elif rem !=0: print "{0} does not divide {1} evelnly".format(mod2, mod1)
 	


def main ():

	prompt = '> '
	print " \n \t\t\t ~ This is python Odd/Even Exercise ~ \n" 
	print "Please input your number: " 
	number = raw_input(prompt)
	print " Your number is: ", number
	print " Is your number even or odd? let's find out!" 

	# get an error :TypeError: not all arguments converted during string formatting
	# make sure you parse the number is a int-type
	number = int(number)				# yep this fixed it

	modcheck(number) 
	
	print " \n\n Now please input two numbers (number) and (check); does check divide number evenly ?  "
	num = raw_input(prompt) 
	check = raw_input(prompt)
	num = int(num)
	check = int(check)
	
	multimodcheck(num,check) 	


# Boilerplate end of the file stuff
if __name__ == '__main__':
  main()
