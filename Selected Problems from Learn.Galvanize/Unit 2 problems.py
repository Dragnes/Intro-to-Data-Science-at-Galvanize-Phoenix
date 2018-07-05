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
