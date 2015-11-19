#!/usr/bin/python -tt
# Copyright billiescodes 2015
# mergesort: a very basic, simple version of sorting an array by
# merging smaller, sorted sections of the array

import sys
import math 

def merge(A, b, c, mid):
	n1 = (mid+1)-b	 # marks lower limit   
	n2 = c - mid	 # marks upper limit
	tmp = []

	Left = []
	for p in range(n1):
		Left.append(A[b+p]) # loops starting w/ low(=b) index in loop
	
	Right = []
	for q in range(n2):
		Right.append(A[mid+1+q])

	# counters to go through arrays Left(i) and Right(j) 
	i = 0 ; j = 0
 

	while i < len(Left) and j < len(Right):   
		
		if Left[i] <= Right[j]:
			tmp.append(Left[i])
			i+=1
		elif Left[i] > Right[j]:
			tmp.append(Right[j]) 
			j+=1

	# add the trailing elements of each half i.e. of Left/Right
	if i <= mid:
		tmp += Left[i:]
	if j <= c:
		tmp += Right[j:]
	
	# copy tmp back into A, the original array
	# cruicial part, whatever is sorted will now be placed at the beginning of array A
	# whenever A is called again recursively 
	z = 0
	while b <=c:
		A[b] = tmp[z]
		b += 1
		z +=1
	
def mergesort(A, b, c):
  # recursively call on mergesort until down to two elements
  
	if b < c:
		mid =int(math.floor((c+b)/2))
		
		#print 'call to mergesort', A, b, mid, c
		mergesort(A, b, mid)			# sort left side of array
		mergesort(A, mid+1,c)			# sort right side of array
		merge(A, b, c, mid)				# merge

def main():
	if len(sys.argv)>= 2:
		A = sys.argv[1]
	else:
		#A = [ 2, 6, 5, 3, 4, 1]
		A = [ 12, 6, 5, 3, 4, 1,7,9,8,13,11,17]
	low = 0
	high = len(A)

	print A
	mergesort(A, low, high-1) 
	
	print "mergesort over; here is the sorted array: "
	print A

 #now call the function main()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
