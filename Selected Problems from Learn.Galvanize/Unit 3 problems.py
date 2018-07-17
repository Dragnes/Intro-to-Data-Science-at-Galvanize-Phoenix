# Write a program that takes a user-inputted non-negative integer and generates an arrow (like this: ->) whose tail is the length of the number.
# For example, if the user inputs 4, your program should print ---->.
# If the user inputs 0, your program should print >. Hint: you'll find the * and + string operations helpful here.

N = int(input('Please enter a number: '))
arrow = '>'
if N == 0:
    print(arrow)
if N > 0:
    print(N*'-' + arrow)

# Write a program that takes a user-inputted string, converts it to all caps and prints it out.
# For example, if the user inputs 'Stop shouting!', your program should print 'STOP SHOUTING!'

s = input('Please enter a string: ')
s = s.upper()
print(s)

# Write a program that takes a user-inputted string and does the following:
# if the string is in all caps, convert it to lower case.
# if this string is not in all caps, convert it to all caps and append 3 exclamation marks. 
# Your program should then print out the converted string.
# For example, if the user inputs 'Hi', your program should print 'HI!!!'.
# If the user inputs 'HELLO', your program should print 'hello'. Hint: you'll find the string method isupper() helpful.

s = input('Please enter a string: ')
if s.isupper():
    s = s.lower()
else:
    s = s.upper() 
    s = s + '!!!'
print(s)

# Write a program that takes a user-inputted string and prints out the character at index 5 (assuming zero indexing).
# If the string has less than 6 characters, your program should print 'String too short.' For example:
# If the inputted string is 'Testing', your program should print 'n'.
# If the inputted string is 'Test', your program should print 'String too short.'
# Hint: You'll find the len() function helpful to test the length of the inputted string.

s = input('Please enter a string: ')
if len(s) > 6:
    print(s[5])
else:
    print('String too short.')

# Write a program that takes a user-inputted string and prints out the substring of characters at the 2nd, 3rd and 4th index position (assuming zero indexing).
# If the string has less than 5 characters, your program should print 'String too short.' For example:
# If the inputted string is 'Testing', your program should print 'sti'.
# If the inputted string is 'Test', your program should print 'String too short.'
# Note: Do not use a while or for loop in your program.

s = input('Please enter a string: ')
if len(s) < 5:
    print('String too short.')
else:
    print(s[2:5])

# Write a program that takes a user-inputted string and prints out every other character from that string, beginning at index 1 (assuming zero indexing).
# If the string has less than 2 characters, your program should print 'String too short.' For example:
# If the inputted string is 'Testing', your program should print 'etn'.
# If the inputted string is 'T', your program should print 'String too short.'
# Note: do not use a while or for loop in your program.

s = input('Please enter a string: ')
if len(s) < 2:
    print('String too short.')
else:
    print(s[1:len(s):2])

# Write a program that takes a user-inputted string and prints out the next-to-last character from that string.
# If the string has less than 2 characters, your program should print 'String too short.' For example:
# If the inputted string is 'Testing', your program should print 'n'.
# If the inputted string is 'T', your program should print 'String too short.'

s = input('Please enter a string: ')
if len(s) < 2:
    print('String too short.')
else:
    print(s[-2])

# The sample below uses a while loop to print out every other character (starting at index 0) from a user-inputted string in uppercase.
# Rewrite the code to use a for loop instead; your program's output should be the same as before.
# Note: Try to write your program without relying using the range() constructor — a much more Pythonic solution is possible.

''' Given while loop '''
s = input('Please enter a string: ')
i = 0
while i < len(s):
    print(s[i].upper())
    i += 2

''' Solution with for loop ''' 
s = input('Please enter a string: ')
for i in s[::2]:
    print(i.upper())

# Write a program that takes a user-inputted string and prints out Hello, <input>! in response, where <input> is the inputted string.
# For example, if the inputted string is 'world', your program should print 'Hello, world!'

s = input('Please enter a string: ')
print('Hello, ' + s + '!')

# Write a program that takes a user-inputted integer and prints out Two times <input> is <result>.
# where <input> is the inputted integer and <result> is twice that value.
# For example, if the user provides the number 10, your program should print 'Two times 10 is 20.'

n = int(input('Please enter an integer: '))
print('Two times {0} is {1}.'.format(n, 2*n))

# Write a program that takes a user-inputted integer and prints out the value of pi to the number of decimal places specified by the integer.
# For example, if the inputted integer is '2' your program should print '3.14'.
# Hints:
# Python's math package includes a constant for pi (as pi). We have imported pi for you in the example code below.
# The format string syntax for rendering a floating point value to N decimal places is {:.Nf}. The example code below prints pi to 10 decimal places.
# You will first need to assemble a format string, and then print your result using that format string.

from math import pi
n = int(input('Please enter an integer: '))
print("{:.{}f}".format(pi, n))
