#!/usr/bin/Python
# -*- coding: utf-8 -*-

# billiescodes 2016
#		Write a program that prints the numbers from 1 to 100. 
# for mulitples of 3 write "fizz" and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”."


	
for a in range(1,101):
	if (a % 3 == 0 and a % 5 ==0 ): print 'fizzbuzz' 
	elif a % 3 == 0: print 'fizz'
	elif a % 5 == 0: print 'buzz'
	else: print a 

