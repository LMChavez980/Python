# Program to read from a file and print the id, title (first only), time and key signature line by line
# 16/10/18
# Louis Chavez


def clean_s(line_cl):  # Function to remove leading and trailing whitespaces using .strip()
    """Remove leading and trailing whitespace"""
    line_cl = line_cl.strip()

    return line_cl


# Open the file in read mode
# Try...else block to test for error
try:
    read_file = open("hnr.abc", "r")

except IOError:
    print("Unable to open file: File doesn't exist")
else:
    print("File is found. Opening for reading.....\n")

    # initialise strings and title counter
    ID = ""
    Title = ""
    Time_sig = ""
    Key_sig = ""
    t_count = int(0)
    all_count = int(0)

    # Loop to read every line of the file
    for line in read_file:
        if line[:2] == 'X:':  # if the line starts w/ 'X:' put it into variable 'ID'
            clean_s(line)
            ID = line[2:len(line)-1]
            print("ID:", ID, end='...')
            continue
        elif line[:2] == 'T:' and t_count is 0:  # if the line starts w/ 'T:' put it into variable 'Title'
            clean_s(line)
            Title = line[2:len(line)-1]
            print("Title:", Title, end='...')
            t_count += 1  # if title counter is more than 1 then don't go into this loop
            continue
        elif line[:2] == 'M:':  # if the line starts w/ 'M:' put it into variable 'Time_sig'
            clean_s(line)
            Time_sig = line[2:len(line)-1]
            print("Time Sig.:", Time_sig, end='...')
            continue
        elif line[:2] == 'K:':  # if the line starts w/ 'K:' put it into variable 'Key_sig'
            t_count = 0
            clean_s(line)
            Key_sig = line[2:len(line)-1]
            print("Key Sig:", Key_sig)
            all_count += 1
        # end if

    # end for

    print("~"*30)
    print("There are", all_count, "tunes in the file")
    print("~"*30)

    read_file.close()  # Always close file in the end



