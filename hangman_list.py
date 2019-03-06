# Hangman Game Program using lists
# 11/10/18
# Louis Chavez

win_word = "secret"  # winning word
win_word = list(win_word)  # turn into list
track_word = "*"*len(win_word)  # progress tracker
track_word = list(track_word)  # turn into list
chance = int(3)  # chance counter

# loop for program - terminates if chance goes below 0 or user wins
while chance > 0:
    print("\nProgress: ", ''.join(track_word))
    print("\nChances:", chance)
    guess = input("\nEnter a word or letter - ")
    match = int(0)

    # if what is entered is a letter
    if (len(guess)) == 1:
        # loop to compare letter with each element
        for i in range(len(win_word)):
            if guess == win_word[i]:
                match += 1  # match counter
                track_word[i] = guess  # insert guess into progress counter
            # end if

        # end for

        # if there is no match
        if match == 0:
            chance -= 1
        # end if

        # if user completes sequence
        if track_word == win_word:
            print("Congratulations you win!")
            break
        # end if

    # end if

    # if what is entered in a string
    elif guess == win_word:
        print("\nCongratulations you win!")
        break
    else:
        chance -= 1
    # end elif

    # print hangman
    if chance == 2:
        print("\nㅇ")
    elif chance == 1:
        print("\n우")
    # end elif

# user loses
else:
    print("\nIt's over you lost 웃")