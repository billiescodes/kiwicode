#!/usr/bin/Python

# billiescodes 2016
# List Overlap Comprehensions ex.10 
# list overlap as before, using list comprehension
# NOTE not entirely finished; didn't add random list gen, that's ok
			# also thinking of doing it a third way below


def main(): 

	print " \n\t\t\t ~ List Overlap Comprehension ~ " 
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

	print "lists a:\t {} \n and b:\t\t {}".format(a,b)  
	
	list_over = [ i for i in a for j in b if i==j  ]
	
	print " \nwith List comprehension; but duplicates allowed \n", list_over

	fin_overlap = []
	for a in list_over:
		if a not in fin_overlap:
			fin_overlap.append(a)
	print "\n w/List Comp; no duplicates \n", fin_overlap	
	
	## Incomplete thought on how to do it with just two Comprehensive lists
	## might try to solve this later
	##fin = [i for i in range(len(list_over))-1 for j in range(len(list_over)) if list_over[i]

#End of file stuff
if __name__=='__main__':	
	main()
