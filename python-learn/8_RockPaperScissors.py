#!/usr/bin/Python

#billiescodes 2016
#RckPaperScissors.py"
# make a two-player Rock-Paper_scissors game
# Ask for player plays(w/input) compare them, 
# print out a message of congratulations to the winner
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import sys
import random

def compare(play,cplay):
# test if player of computer win
	print "computer plays: ", cplay
	if play==cplay:
		return 'tie' 
	if play=='rock' and cplay=='scissors':
		return 'player'
	if play=='rock' and cplay=='paper':
		return 'computer'
	if play=='scissors' and cplay=='paper':
		return 'player'
	if play=='scissors' and cplay=='rock':
		return 'computer'
	if play=='paper' and cplay=='rock':
		return 'player'
	if play=='paper' and cplay=='scissors':
		return 'computer' 

def comp_play(num):
	if num%3==0:
		c_play='rock'
	elif num%2==0:
		c_play='paper'	
	else:
		c_play='scissors'
	return c_play

def main():

	print "\n\t\t\t ~ Rock Paper scissors ~ "


	#NOTE try a while(True) statement with an else: clause
	while(True):			#run the loop of asking player for input
		prompt='>'
		print "Please enter your play (rock/paper/scissors) :: press q, or quit to quit"
		play=str(raw_input(prompt)).lower()
		if play=='q' or play=='quit':sys.exit(1) 
		if play!='rock' and play!='scissors' and play!='paper':
			print "please enter a valid choice! " 		
			continue

		print "Your play choice is '{}' ".format(play)
		
		##randomly generate choice decision for who wins 
		# numbers 1-99 are inclusive, equal probability for picking multiple of 1,2, or 3 
		num = random.randrange(1,100)
		counter_play = comp_play(num) 
		winner=compare(play, counter_play)

		if winner !='tie':
			print "\n the winner is: {} !!! ".format(winner.upper())
			continue
		else: # winner=='tie'
			print "\n It's a tie! Try again!" 
			continue

#End of file
if __name__=='__main__':
	main()
