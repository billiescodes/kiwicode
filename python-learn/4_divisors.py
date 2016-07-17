#!/usr/bin/Python

# billiescodes 2016
# Exercise 4: Divisors	(FOCUS: functions)
	# a few alternates: NOT a billiescodes codes


# 1. Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
		# 13 is a divisor of 26: 26/13 no remainder
# 2. obviously this code will have an upper limit on divisors, you have limited RAM, guurl!  
# 3. write in an exception for when it's not a number

def test_int(num):
	#use an exception
	try:
		num = int(num)
		return num
	except:
		print "not a number; try again  "
		return 'nothing'

def divisor_test(num):
	nu = []	
	#create my big big list of possible divisors!
	biglist = range(2,99999)
	for i in biglist: 
		tmp = num % i					 #NOTE: not 'biglist(i)' >> () is a function call, but biglist is a LIST	 
		if tmp == 0: nu.append(i)
	return nu

 

def main():
	print " \n \t\t\t ~ Divisors program ~ \n" 
	print "please input a number (type 'quit', 'exit', or 'q' to exit): "

	while True:								#NOTE: this loop will run unil the loop either returns somthing, or break 
		prompt = '>'
		inpt = raw_input(prompt)
		if (inpt == 'quit') or (inpt == 'exit') or (inpt == 'q'):
			break
		num_usr = test_int(inpt)
		if num_usr == 'nothing' : continue
	
		print "\n your divisors are: "
		zaba = divisor_test(num_usr)	
		print zaba



# Boilerplate end of file stuff
if __name__ == '__main__':
	main()

