#Write an if-else statement that...
#
#decrements x by 1 if x is less than or equal to 10, and
#increments x by 1 otherwise.
if x <= 10:
    x -= 1
else:
    x += 1

#Write an if-elif-else statement that...
#
#decrements x by 5 if x is greater than 20,
#increments x by 5 if x is less than 10, and
#multiplies x by 5 otherwise.
if x > 20:
    x -= 5
elif x < 10:
    x += 5
else:
    x *= 5
    

#Write an if-else statement that...
#
#increments x by 5 if x is greater than or equal to 10 and less than or equal to 20,
#increments x by 1 otherwise.
if x >= 10 and x <= 20:
    x += 5
else:
    x += 1

#Write an if-else statement that...
#
#prints yes if x equals 2 or 4,
#prints no otherwise.
if x == 2 or x == 4:
    print('yes')
else:
    print('no')

#Write an if-else statement that...
#
#prints out of range if x is not within the range [5, 10] (inclusive),
#prints the value of x otherwise.
if x not in range(5, 10):
    print('out of range')
else:
    print(x)

#Write a while loop that calculates the sum ∑(from i-10) = 10i, and prints the result.
i = 0
total = 0
while i <= 10:
    total += 10*i
    i += 1
print(total)

#Write a while loop that counts down from 5 to 1 and prints out its countdown as it goes.
i = 6
while i > 1:
    i -= 1
    print(i)

#Write a while loop that calculates the sum of the integers from 1 to 20 (inclusive), excluding those integers evenly divisible by 3.
#(Hint: You'll find the modulo operator (%) and the continue statement handy for this.)
#Print the result of your calculation at the end of your code.
i = 1
total = 0
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    total += i
    i += 1
print(total)

#Write a while loop that calculates the product of the integers from 1 to 20
#but which stops after the accumulated product exceeds 1 billion (1000000000).
#Print the value of your calculated product afterward.
i = 1
product = 1
while i < 21:
    product *= i
    i += 1
    if product >= 1000000000:
        break
print(product)

#The following program is supposed to print the integers from 1 to 9, excluding 3, 5 and 7
i = 1
while i < 10:
    if i == 3 or i == 5 or i == 7:
        pass
    else:
        print(i)
    i += 1

#Write a script that takes two user inputted numbers and prints "The first number is larger" or "The second number is larger" depending on which is larger.
#If the numbers are equal, print "The two numbers are equal". (Hint: you'll need to use input() twice.)
first_number = int(input('Please enter a number: '))
second_number = int(input('Please enter another number: '))
if first_number > second_number:
    print('The first number is larger.')
elif first_number < second_number:
    print('The second number is larger.')
else:
    print('The two numbers are equal.')

#Write a script that computes the factorial of a user inputted positive number and prints the result. 
#Things to think about:
#What is the process of computing a factorial if you were to compute it by hand?
#What is the common starting place when trying to compute the factorial of any number?
#What should your code do if the user inputs a number that isn't positive?
number = int(input('Please enter a number: '))
total = 1
while number > 0:
    total *= number
    number -= 1
print(total)

number = int(input('Please enter a number: '))
result = 1
count = 1
while count <= number:
    result *= count
    count += 1
print(result)

#Write a script that computes and prints all of the positive divisors of a user inputted positive number from lowest to highest.
#Things to think about:
#How do you determine if a single number is a divisor of another?
#How do you do this multiple times? (Hint: it involves a while loop.)
#When do you stop the loop?
number = int(input('Please enter a number: '))
for i in range(1, number + 1):
    if number % i == 0:
        print(i)

number = int(input('Please enter a number: '))
check = 1
while check <= number:
    if number % check == 0:
        print(check)
    check += 1

number = int(input('Please enter a number: '))
check = 1
while check <= number / 2:
    if number % check == 0:
        print(check)
    check += 1
print(number)

#Write a script that computes the greatest common divisor between two user inputted positive numbers and prints the result.
#Things to think about:
#How do you get two numbers from the user?
#Where should you start your search for the GCD?
#Where/how should you end your search?
first = int(input('Please enter a number: '))
second = int(input('Please enter a number: '))
if first > second:
    selected = first
else:
    selected = second
for i in range(1, selected):
    if (first % i == 0) and (second % i == 0):
        divisor = i
print(divisor)

number = int(input('Please enter a number: '))
number2 = int(input('Please enter another number: '))
while number != number2:
    if number > number2:
        number -= number2
    else:
        number2 -= number
print(number)

number = int(input('Please enter a number: '))
number2 = int(input('Please enter another number: '))
while number2 != 0:
    temp = number2
    number2 = number % number2
    number = temp    
print(number)

while number2 != 0:
    number, number2 = number2, number % number2
print(number)

#Write a script that computes the least common multiple between two user inputted positive numbers and prints the result.
#Things to think about:
#How do you get two numbers from the user?
#Where should you start your search for the LCM?
#Where/how should you end your search?
number1  = int(input('Please enter a number: '))
number2 = int(input('Please enter another number: '))
if number1 > number2:
    greater = number1
else:
    greater = number2
while(True):
    if((greater % number1 == 0) and (greater % number2 == 0)):
        lcm = greater
        break
    greater += 1
print(lcm)

number = int(input('Please enter a number: '))
number2 = int(input('Please enter another number: '))
a, b = number, number2
while number != number2:
    if number > number2:
        number -= number2
    else:
        number2 -= number
result = (a / number) * b
print(result)

#Write a script that determines whether or not a user inputted number is a prime number and prints
#"The number you inputted is a prime number" or "The number you inputted is not a prime number" depending on what your script finds. 
#Things to think about:
#How do you check if a number is divisible by another number?
#What numbers are a prime number divisible by?
#How do you check all of the numbers a number could be divisible by (Hint: use a loop)?
#When do you stop the loop?

num = int(input('Please enter a number: '))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("The number you inputted is not a prime number.")
           break
   else:
       print("The number you inputted is a prime number.")
       
number = int(input('Please enter a number: '))
check = 2
is_prime = True
while check <= number / 2:
    if number % check == 0:
        print('The number you inputted is not a prime number.')
        is_prime = False
        break
    check += 1
if is_prime:
    print('The number you inputted is a prime number.')
