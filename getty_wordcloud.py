# Program that will analise a file word words and create a word cloud web page using html
# 7/11/18
# Louis Chavez


def process_line(line, wfr_dict):
    """Function to process lines in the file"""
    import string
    # iterate through lines in text file
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        # ignore '--' in file
        if word != '--':
            word = word.lower()
            word = word.strip()
            # remove commas, periods and other punctuations
            word = word.strip(string.punctuation)
            retval = check_stp(word)  # check if word is a stop word
            if retval == 0:
                wfr_dict = add_word(word, wfr_dict)
            # end if
        # end if
    # end for
    return wfr_dict
# end process


def check_stp(word):
    """Function to check if a word is a stop word"""
    import string
    stp = open("stopwords.txt", "r")
    val = 0
    for stp_word in stp:
        stp_word = stp_word.lower()
        stp_word = stp_word.strip()
        stp_word = stp_word.strip(string.punctuation)
        stp_word = stp_word.strip(string.whitespace)
        if stp_word == word:
            val = 1
        # end if
    # end for
    stp.close()
    return val
# end check_stp


def add_word(w1, dict1):
    """Function to add word to dictionary"""
    if w1 in dict1:
        dict1[w1] += 1
    else:
        dict1[w1] = 1
    # end if
    return dict1
# end add_word


def make_wp(x, webpage, wfr_dict):
    """Function to create a word cloud web page using html"""
    webpage.write("<!DOCTYPE html>\
    <html>\
    <head lang=\"en\">\
    <meta charset=\"UTF-8\">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style=\"text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; \
    border:1px solid black\">\"\n")

    for word in wfr_dict:
        x = 10
        x = str(x)
        if wfr_dict[word] > 1:
            x = int(x)
            x = x * int(wfr_dict[word])
            x = str(x)
        # end if
        webpage.write("<span style=\"font-size: ")
        webpage.write(x)
        webpage.write("px\">")
        webpage.write(word)
        webpage.write(" </span>\n")
    # end for

    webpage.write("</div>\
    </body>\
    </html>")

# make_wp


def main():
    gettys = open("gettysburg.txt", "r")
    word_freq_dict = {}
    for line in gettys:
        word_freq_dict = process_line(line, word_freq_dict)
    # end for
    x = int(10)
    webpage = open("gettysweb.html", "w")
    make_wp(x, webpage, word_freq_dict)

    gettys.close()
    webpage.close()
# end main


main()

