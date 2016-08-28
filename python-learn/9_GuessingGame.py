#!/usr/bin/Python

#billiescodes 2016
# "9_GuesingGame.py", part 1
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then 
#tell them whether they guessed too low, too high, or exactly right

import random
import sys

def main():

	print " \n\t\t\t	~ Guessing Game Part 1 ~ "

	# Game Loop
	while(True): 
		print "the Random Number is between 1 and 9 (inclusive) type 'q' to exit"
		guess = random.randrange(1,10)
		counter=1	

		# Guess Loop
		while(True):
			print "input your guess: "
			prompt='>'
			
			# Input Loop
			while(True):
				try: 
					usr_prompt = raw_input(prompt)
					if usr_prompt=='q': sys.exit('Goodbye!') 
					usr_prompt=int(usr_prompt)
					if usr_prompt not in range(1,10):
						print "Please input a valid guess; numbers 1-9"
						continue
					break
				except ValueError: 
					print ("Ooos! Not a valid number.\n Please input a valid guess; numbers 1-9" )
		 
			if usr_prompt==guess: 
				print "congrats! you've guessed the number: ", guess
				break
			elif usr_prompt>guess:
				counter+=1
				print "your guess is too high; try again"
				continue
			elif usr_prompt<guess:
				counter+=1 
				print "your guess is too low; try again"
				continue 
		
		print " \n Your guess took {} trials. Would you like to play again (y/n)?".format(counter) 
		
		# Play Again loop
		while(True):
			play_again= str(raw_input(prompt))
			if play_again!='y' and play_again !='n': 
				print "would you like to play again? (y/n)"	
				continue
			elif play_again=='y':
				break
			elif play_again=='n': 
				sys.exit('Goodbye!')


	print " \n End of program" 
#End of File Stuff
if __name__=='__main__':
	main()


