# Program to scramble a word - keeping first and last letter
# 4/10/18
# Louis Chavez

import random  # predefined random sequences

s = input("Enter a word - ")

# Manual method

print("\nManual method - random letters produced with repetition \n")

first = s[:1]  # slice string for beginning only
l = len(s)
last = s[l-1]
mix = s[1:l-1]  # slice string for only middle

print(first, end='')  # end='' print on same line

# Loop to print out string elements randomly

for index in range(len(mix)):
    i = random.randint(0, (len(mix)-1))  # generate random number between 0 and 8
    print(mix[i], end='')

# End for

print(last)

# Auto

print("\nUsing the list + random.shuffle method - random letters but no repeat \n")

mix2 = list(mix)
random.shuffle(mix2)

print(first+''.join(mix2)+last)

# The method join() returns a string in which the string elements of sequence have been joined by str separator.

