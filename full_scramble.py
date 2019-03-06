# Program to scramble a sentence
# 7/10/18
# Louis Chavez

import random
import string

s = input("Enter a sentence - ")
list_words = s.split()

# Scramble words

for word in list_words:
    # make sure word can be scrambled, more that 3 characters
    if len(word) > 3:

        l = len(word)
        first = word[:1]
        last = word[l - 1]

        # check for single punctuation in the end of sentence

        if last in string.punctuation:
            fins = last
            last = word[-2]
            mix = word[1:l-2]
            edit = list(mix)
            random.shuffle(edit)
            print(first + ''.join(edit)+last+fins, end=' ')

        else:
            mix = word[1:l - 1]
            edit = list(mix)
            random.shuffle(edit)
            print(first + ''.join(edit) + last, end=' ')

        # end if else
    else:
        print(word, end=' ')

    # end if else

# end for
