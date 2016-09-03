#!/usr/bin/Python

#billiescodes 2016
#Write a program (function!) that takes a list and returns a new list that contains 
# all the elements of the first list minus all the duplicates.
# do this using sets 

def rem_dupes(lista):
	#takes a list, returns a set w/o dupes
	numbers=set()
	
	for a in lista:
		if a not in numbers: 
			numbers.add(a)	
	return numbers


def list_and_sort(set_a):
	#takes a set, returns sorted list
	nulist=list(set_a)
	nulist.sort()			#NOTE do not have to re-assign nulist just run method on it
	return nulist

def main():

	print " \n\t\t\t ~List Remove duplicates ~ " 
	a = [1, 4, 4, 4,9,9,9, 16, 25, 36, 36, 49, 64, 81,81, 100]
	
	print " test list: \n ", a

	nulist = rem_dupes(a)
	nulist=list_and_sort(nulist)

	print " no dupes : ", nulist

#End of file stuff
if __name__=='__main__':
	main()
