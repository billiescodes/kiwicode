#!/usr/bin/python -tt


import sys
import math

def main():
	A = [ 2, 8, 7, 5, 3, 4, 1]
	c = len(A)
	b = 0 

	n1 = int(math.floor(((b+c)/2)))+1
	print n1
	tmp = []

	Left = []
        for c in range(n1):
                Left.append(A[b+c])
	
	print Left
	i=2

	tmp +=Left[i:]
	print tmp 

 	again = []
	again += Left[:i]
	print again
	
#now call the function main()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
        main()


