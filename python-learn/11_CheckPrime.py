#!/usr/bin/Python

# billiescodes 2016
# CheckPrime.py ex.11
 
#Ask the user for a number and determine whether the number is prime or not.

### function checks if input is prime
def checkprime(num):
	nu=[]
	for i in range(1,num+1):
		if num%i ==0: nu.append(i)	
	print "divisors: ", nu
	if len(nu)== 2: return 'prime'



def main():

	print "\n\t\t\t ~ Check Primality Program ~ "
	while(True):
		inpt = checknum()		
		if inpt == 'none': continue
		else: break

	check =checkprime(inpt)
	if check == 'prime': print "the number is a prime"
	else: print "not a prime" 



### function checks input as integer
def checknum():
	inpt = raw_input("please input a number, (floats will be rounded up or down) \n",)
	try:
		inpt=int(round(float(inpt)))		#will convert floats to ints as well
		return inpt
	except:
		print "Not a valid number, please try again" 
		return 'none' 

#End of file stuff
if __name__=='__main__':
	main()
 
