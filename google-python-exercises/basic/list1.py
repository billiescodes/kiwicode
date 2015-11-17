#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
  #initialize counter
  counter = 0 
  #length = len(words) #length of list

  # for <length of string> loop through
  for var in words:
    length = len(var)
    #print var, ' ',len(var)
    
	## how to loop over all the letters
    # i=0
    # while i < len(var):      
    #  print var[i]  
    #  i +=1

# print var[len(var)]
    if len(var) >= 2:
      if var[0] == var[len(var)-1]:
        counter += 1; 

  # if <length of string> is > 2 
  # AND if string(0)== string(last) add counter 

  return counter


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++ pseudocode +++
  # 1. loop through list, start nulist1, nulist 2
  # 2. if var[0] == x group first, by puttin into nulist1
	## use instead var.startswith(x) method!	
  # 3. to sort alphabetically place into nulist2
	## 
# ['bbb', 'ccc', 'axx', 'xzz', 'xaa']

  tmp1 = []		# sort words that begin with x here
  tmp2 = []		# sort alphabetic words here
 
  for var in words:
    
    # check first letter of var in words if it's x
    # here can also use method var.startswith('x') 
    if var[0] == 'x': 
      tmp1.append(var)
     #DEBUG print 'this is it', var 
    else:
      tmp2.append(var)
    #DEBUG print sorted(tmp1), 'pause ',  sorted(tmp2)
  
  total =  sorted(tmp1) + sorted(tmp2)
  return total



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  # +++your code here+++
   
  # you can define another function last, but it has to be outside this function
  # then call last in this function, in this case in the return statement
  # remember key takes in a function, as argument, like len(), in this case it's last
  return sorted(tuples,key=last)

def last(s):
  return s[-1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'match_ends'
 # test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
 # test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
 # test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
