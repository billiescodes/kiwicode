#!/usr/bin/python -tt

import sys
import math 

def merge(A, b, c, mid):
	n1 = (mid+1)-b # midpoint(+1) - low index value 
	n2 =  c+1 - mid # high- mid index
	tmp = []
	print '1: ', A

	##if b == 0:
	##	sys.exit()
	##	return 
	#break

	Left = []
	for p in range(n1):
		Left.append(A[b+p]) # loops starting w/ low(=b) index in loop
	
	Right = []
	for q in range(n2):
		Right.append(A[mid+1+q])
	print Right
	print Left
	
	print '7: ', tmp, len(Left), len(Right)

	# counters to go through array; i/j only go through half of array
	i = 0 ; j = 0
 
	print '2: enter mergesort', i , j , c
#	print 'left array, ith elemnt before for loop:  ', Left[i]

	while i <= mid and j <= c:   
		print '3: enter while loop ', i, j, mid, c
		# takes care of comparing L and R
		if Left[i] <= Right[j]:
			tmp.append(Left[i])
			i+=1
			print '4: here', tmp, i
				 
		elif Left[i] > Right[j]: 	# the <= comparison takes care of itLeft[i] > Right[j]:
			tmp.append(Right[j]) 
			j+=1
			print '5: not here', tmp, j 
	print '6: does my brave code make it out here? ', i, j 
	
#	if len(tmp) < 2:
#		return a

	print '7: ', tmp, len(Left), len(Right)
	
	if i <= mid:
		tmp += Left[i:]
	if j <= c:
		tmp += Right[j:]
	
#	if len(tmp) < 2; 

        print 'tmp is now', tmp
	z = 0
	while b <=c:
		A[b] = tmp[z]
		print '8:  here?'
		b += 1
		z +=1
		if c < 7:
			print "LAST"
		break 
	print  '9: end of code, tmp, A:', tmp, A
	
 
    #break

	#return tmp	
	#if there are trailing elements e.g. (1 2 3 5) merge with (4 6 7 8)
	# DO NOT re-initialize i or k at this point 
	
def mergesort(A, b, c):
  # recursively call on mergesort until down to two elements
#	mid =int(math.floor((c+b)/2))

#	if mid >1:
		#print  'low= ', b, 'mid ', mid, 'high= ', c 
	if b < c:
		mid =int(math.floor((c+b)/2))
		print  'low= ', b, 'mid ', mid, 'high= ', c
		
		print 'call to mergesort', A, b, mid, c
		mergesort(A, b, mid) # sort left side
		print A, b, mid, c
		mergesort(A, mid+1,c)	# sort right side
		print A, b, mid, c
		merge(A, b, c, mid)	# merge

def main():
	print 'something' 
	if len(sys.argv)>= 2:
		A = sys.argv[1]
	else:
		A = [ 2, 6, 5, 3, 4, 1]
		
	low = 0
	high = len(A)

	print A
	print "here is: low, high, index", low, high
	mergesort(A, low, high-1) 
		 # high-1, because of array indexing start at 0 I think

	print A

 #now call the function main()
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
