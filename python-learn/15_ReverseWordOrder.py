#!/usr/bin/Python

#biliescodes 2016
# reverse word order
#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.


def split_n_reverse(mystring):
	teststring=mystring.split(" ")
	tmp = [a for a in reversed(teststring) ]

	return tmp


def main():

	print "\n\t\t\t ~ Reverse Word order ~ "	
	inpt = str(raw_input("Please input a long string/sentence: \n> ",))
	print "your input isi '{}'".format(inpt)

	tmplist=split_n_reverse(inpt)
	result = " ".join(tmplist)

	print "Reversed order: \n", result


if __name__=='__main__':
	main() 