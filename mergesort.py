#!/usr/bin/python -tt

import sys
import math 

def merge(a, b, c, mid):
#initialize array
	#-----> this doesn't work! 	#Left=a[:mid], Right=a[mid:] 
	n1 = (mid+1)-b # midpoint(+1) - low index value 
	n2 =  c - mid # high- mid index

	Left = []
	for c in range(n1):
		Left.append(a[b+c]) # loops starting w/ low(=b) index in loop
	
	Right = []
	for d in range(n2):
		Right.append(a[mid+1+d])

	# counters to go through array
	i = b ; j = mid
	k = 0  
	#print i, j

	for k in range(b,mid+1):
	#while i < mid and j < c:   
		# takes care of comparing L and R
		if Left[i] < Right[j]:
			a[k] == Left[i]
			i=i+1; 
		else Left[i] > Right[j]:
			a[k] == Right[j] 
			j=j+1
		k=k+1
		break
	
	#if there are trailing elements e.g. (1 2 3 5) merge with (4 6 7 8)
	# DO NOT re-initialize i or k at this point 
	while i<len(Left):
		a[k] = Left[i]
		i = i+1
		k = k+1 
		
	while j<len(Right):
		a[k] = Right[j]
		j = j+1
		k = k+1
	
'''         #put the two arrays together
	for i in k
		a[i] = D[i]	
'''
	
def mergesort(a, b, c):
  # recursively call on mergesort until down to two elements
	mid =int(math.floor((c+b)/2))

	#print  'low= ', b, 'mid ', mid, 'high= ', c 
	while b < c:
		mergesort(a, b, mid)
		mergesort(a, mid+1,c)
		merge(a, b, c, mid)	

def main():
	print 'something' 
	if len(sys.argv)>= 2:
		A = sys.argv[1]
	else:
		A = [ 1, 8, 7, 5, 3, 4, 2]
		
	low = 0
	high = len(A) -1

	print A
	print "here is: low, high, index", low, high
	mergesort(A, low, high)

	print A

 #now call the function main()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
