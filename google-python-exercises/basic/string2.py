#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  if len(s) >= 3 and s[-3:] !='ing':
    s_verb = s + 'ing'  
  elif len(s) >= 3 and s[-3:] == 'ing':
    s_verb = s + 'ly' 
  elif len(s) <3: 
    s_verb = s 
    
  return s_verb


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  
  index_not = s.find('not')
  index_bad = s.find('bad') 

	# make sure that neither of the indeces is -1, 
    # eg. if the string is 'adaba', it will find 'bad' starting at -1
 
  if index_bad > index_not and index_bad != -1 and index_not -1:			
		# if 'bad' follows 'not'
    sub = s[index_not : index_bad+3] # the whole string ends after index_bad+3
    print sub
    new_string = s.replace(sub,'good')
  else:
    new_string = s

  return new_string


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++

  # test if even or odd with modulo operator 
  if len(a)%2 == 0:			 # even
    half = len(a)/2
    a_front = a[0:half]
    a_back = a[half:]
  elif len(a)%2 ==1:			# odd: define half as first half bigger by onec	
    half_odd = (len(a)+1)/2
    a_front = a[0:half_odd]
    a_back = a[half_odd:]

  if len(b)%2 == 0:			# if string b is even
    half_b = len(b)/2
    b_front = b[0:half_b]
    b_back = b[half_b:]
  elif len(b)%2 == 1:		# if string b is odd
    half_bodd = (len(b)+1)/2
    b_front = b[0:half_bodd]
    b_back = b[half_bodd:]

  print a_front, ' ', a_back
  print b_front, ' ', b_back

  return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
