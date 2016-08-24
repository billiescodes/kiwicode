#!/usr/bin/Python

# billiescodes 2016
# Exercise 6:	String lists 
# ask the user for a string, print out whether string is palindrome or not, level, rotor, kayak


def palindrome(word):
	#work here
	check=False

	for i in range(len(word)):
		if word[i]==word[-i-1]:
			check=True
		else:
			check=False
	return check


def main():

	print " \n\t\t\t ~ String lists program ~ "
	inpt = raw_input(" Please enter a word: ",) 
	inpt = str(inpt)
	print " you entered: ", inpt

	is_palindrome = palindrome(inpt) 

	if is_palindrome:
		print "your input Word is a palindrome"
	else:
		print " nope, sorry bub" 


# Boilerplate end of file stuff
if __name__ == '__main__':
  main()
