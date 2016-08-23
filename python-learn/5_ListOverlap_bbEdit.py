#!/usr/bin/Python

# billiescodes 2016
# Ex. 5 List overlap

# Take two lists, and return a list that contains only the elements that are common b/w the lists (no duplicates)
# should work on lists of diff sizes
## NOTE program WORKS, but want to generate list of RANDOM STRINGS
 
import sys
import random

def simpleCompare(lista,listb): # NOTE: the original simple function I wrote
	# for lists of same length
	tmp = []
	for var in lista: 
		if var in listb:
				if var not in tmp:
					tmp.append(var)
	
	return tmp
############################### learn: for var in A and B #################################
### NOTE same as simpleCompare but faster
def fastCompare(lista,listb):
	tmp=[]
	for var in lista and listb:
		if var in lista and listb: 
			tmp.append(var)
	return tmp

def randgen(length):
	# NOTE 2 ways of generating a random list
	print "enter rand", length
	listC = []
	listD = []  
	## FIRST method
	for i in range(length): 
		a = random.randrange(1,50)
		listC.append(a)	
	## SECOND method 
	listD = [random.randrange(1,50) for i in range(length) ]
	print listC
	print listD
	
	return listC, listD


def main():

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	x = a[:6] #testlengths
	y = b[:7]

	################################### start #############################################
	print "\n \t\t\t ~ List overlap ~ \n "
	
	# boolean flag to ok Random-gen lists 
	randoflag=False
	if len(sys.argv) != 1:
		print "rando?", sys.argv[1] 
		if sys.argv[1] == 'rando': randoflag = True
	else:
		print " for two RANDOM generated lists, give second argument 'rando' "
		print " there are {} arguments in ListOverlap.py".format(len(sys.argv)+1) 

	############# forRando= True, run rando function
	if randoflag==True:
		listlen = 12
		#randgen(listlen) 
		list1,list2 = randgen(listlen)
		overlapList =  fastCompare(list1,list2)
		print " \n the overlap of 2 random Generated lists is: \n", overlapList

	############ forRando= False
	if randoflag==False:
		print "\n fast compare on 2 lenghts: "
		print a, b
		overlapList = fastCompare(a,b)
		print "\n", overlapList 	

###################################### strings #######################################
	
	words1 = ['alice', 'in','wonderland']
	words2 = ['ok','computer','kidA','pablo','honey', 'in']
	print "\n\n\t\t\t ~~ test List of Strings ~~ "
	sameWords = fastCompare(words1,words2)
	
	print "lists are: ", words1, words2 
	print " the same words are: \t" , sameWords



# Boilerplate end of file stuff
if __name__ == '__main__':
  main()
