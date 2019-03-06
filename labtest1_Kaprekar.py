# Program that will prompt user for a number n and print all the Kaprekar numbers from 10 to n
# 1/11/18
# Louis Chavez
# Modified after lab test


def checknum(num):
    """Function to check for kaprekar numbers within limit num"""
    kap_list = []  # list for kaprekar numbers
    for i in range(10, num+1):
        res = i**2  # square
        res = str(res)  # turn into string
        l = len(res)  # get length
        j = l-1
        # Modification here
        while j > 0:
            h1 = res[:(l-j)]
            h2 = res[(l-j):]
            h1 = int(h1)
            h2 = int(h2)
            if h1 + h2 != i:
                j -= 1
            else:
                kap_list.append(i)
                break
            # end if
        # end while
    # end for
    return kap_list
# end checknum


def main():
    num1 = input("Enter number limit - ")
    num1 = int(num1)
    kap_list = checknum(num1)
    print("The list of all Kaprekar numbers from 10 to", num1, ": ")
    for i in kap_list:
        print(i, end=' ')
    # end for
# end main


main()
