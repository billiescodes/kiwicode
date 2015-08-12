#!/usr/bin/python -tt

import sys
import math 

def merge(a, b, c, mid):
	n1 = (mid+1)-b # midpoint(+1) - low index value 
	n2 =  c - mid # high- mid index
	tmp = []
	print a

	Left = []
	for c in range(n1):
		Left.append(a[b+c]) # loops starting w/ low(=b) index in loop
	
	Right = []
	for d in range(n2):
		Right.append(a[mid+1+d])

	# counters to go through array; i/j only go through half of array
	i = b ; j = mid
 
	print 'enter mergesort', i , j , c
#	print 'left array, ith elemnt before for loop:  ', Left[i]

	#	for k in range(b,mid+1):
	while i <= mid and j <= c:   
		print 'enter while loop '
		# takes care of comparing L and R
		if Left[i] <= Right[j]:
			tmp.append(Left[i])
			i+=1
			print 'here'
			break	 
		else: 	# the <= comparison takes care of itLeft[i] > Right[j]:
			tmp.append(Right[j]) 
			j+=1
			print 'not here'

	print ' does my brave code make it out here? ', i, j 
	
#	if len(tmp) < 2:
#		return a

	tmp += Left[i:]
	tmp += Right[j:]
	
#	if len(tmp) < 2; 

        print 'how about here?'

	for i in range(b,c):
		a[i] = tmp[i]
		print ' here?' 

	print  'end of code', tmp[0]
	return tmp	
	#if there are trailing elements e.g. (1 2 3 5) merge with (4 6 7 8)
	# DO NOT re-initialize i or k at this point 
'''     
 	print 'k is ', k
	
	print 'i is ', i 
	print 'j is ', j
'''
	### if not all elements of Left[] were used
#	while i<len(Left):
#		tmp[k] = Left[i]
#		i = i+1
#		k = k+1 
#	break
	### if not all elements of Right[] were used
#	while j<len(Right):
#		tmp[k] = Right[j]
#		j = j+1
#		k = k+1
#	break

#	for i in range(b,c):
#		a[i] = tmp[i]

'''         #put the two arrays together
	for i in k
		a[i] = D[i]	
'''
	
def mergesort(a, b, c):
  # recursively call on mergesort until down to two elements
	mid =int(math.floor((c+b)/2))

	if mid >1:
		print  'low= ', b, 'mid ', mid, 'high= ', c 
	while b < c:
		mergesort(a, b, mid) # sort left side
		mergesort(a, mid+1,c)	# sort right side
		merge(a, b, c, mid)	# merge

def main():
	print 'something' 
	if len(sys.argv)>= 2:
		A = sys.argv[1]
	else:
		A = [ 2, 8, 7, 5, 3, 4, 1]
		
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
