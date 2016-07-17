#!usr/bin/Python

# billiescodes 2016
# Exercise 4: Divisors (FOCUS: as short as possible) 

# with help of some other codes, try to write program 4 in as few lines as possible
	# 1. envelope the entire thing in a while == True loop
	# 2. write for-loop containing remainder-conditional in a list []
	# 3. use the .format method on  print statement to print out the list 
	# 4. have a plan for empty list >> if len(list) > 1, prime number
	# 5. use exception if not a number

def main():
	
	print " \n \t\t\t Alternate Divisors file, (type 'q' to quit)" 
		 ######## the syntax for for-loop within list [ ] is list = [d for a in (...) if x == y ]
				# >> THEN for all items in (...), which becomes lenght(list), d is added if condition x==y is met

	while True:
		inpt = raw_input(" Please input a number: \n",)
		if inpt== 'q': break
		try:  
			inpt = int(inpt)		
			list = [ d for d in range(1,9999) if inpt % d == 0 ]
			if len(list) > 2: print " the divisor list for {} is {}".format(inpt, list) 
			else:  print str(inpt) + " is a prime number" 

		except ValueError:
			print ("Not a number! please input an integer!") 
			continue

# Boilerplate end of file stuff
if __name__ == '__main__':
	main()
