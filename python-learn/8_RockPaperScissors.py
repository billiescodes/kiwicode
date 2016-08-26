#!/usr/bin/Python

#billiescodes 2016
#RckPaperScissors.py"
# make a two-player Rock-Paper_scissors game
# Ask for player plays(w/input) compare them, 
# print out a message of congratulations to the winner

def main():

	print "\n\t\t\t ~ Rock Paper scissors ~ "

	#while(True) run the loop of asking player for input
	prompt='>'
	print "Please enter your play (rock/paper/scissors)"
	play=str(raw_input(prompt))
 
	print "Your play choice is '{}' ".format(play)

#End of file
if __name__=='__main__':
	main()
