# Program that will find the gcd, lcm, add/subtract/reduce fractions
# Fractions will be made in the form of tuples
# 25/10/18
# Louis Chavez


# Euclid's Algorithm: b = a(q) + r
def cal_gcd(m, n):
    """Function to find gcd using Euclid's Algorithm"""
    r = int(1)

    # Loop to find gcd
    while r != 0:
        q = n//m
        r = n-(m*q)
        if r == 0:
            continue  # go back to condition
        n = m
        m = r
    # end while

    return m
# end cal_gcd


# lcm(a, b) = a*b/gcd(a,b)
def cal_lcm(m, n, x):
    """Function to find lcm from gcd"""

    val = int((m*n)/x)

    return val
# end cal_lcm


# adding fractions
def add_frac(f1, f2):
    """Function to add fractions"""
    # take the denominators
    v1 = f1[1]
    v2 = f2[1]

    # get gcd and lcm
    s1 = cal_gcd(v1, v2)
    s2 = cal_lcm(v1, v2, s1)

    # get the numerators (converted)
    i = int(f1[0]*(s2/v1))
    j = int(f1[0]*(s2/v2))

    num = i+j
    total = num, s2

    return total
# end add_frac


# subtracting fractions
def sub_frac(f1, f2):
    """Function to subtract fractions"""
    # take the denominators
    v1 = f1[1]
    v2 = f2[1]

    # get gcd and lcm
    s1 = cal_gcd(v1, v2)
    s2 = cal_lcm(v1, v2, s1)

    # get the numerators (converted)
    i = int(f1[0] * (s2 / v1))
    j = int(f1[0] * (s2 / v2))

    num = i - j
    total = num, s2

    return total
# end sub_frac


# simplify a fraction (reduce)
def reduce_frac(f1):
    """Function that will put the fraction into it's simplest form"""
    m = f1[0]  # numerator into m
    n = f1[1]  # denominator into n

    # get gcd
    div = cal_gcd(m, n)

    m = int(m/div)
    n = int(n/div)

    simp = m, n

    return simp
# reduce_frac


# main
a = int(18)
b = int(60)

# call cal_gcd
gcd = cal_gcd(a, b)
print("\ngcd(", a, ",", b, ") =", gcd)

# call cal_lcm
lcm = cal_lcm(a, b, gcd)
print("lcm(", a, ",", b, ") =", lcm)

# initialise tuples

frac1 = 1, 4
frac2 = 1, 3
frac3 = 50, 100

# call add_frac
add_res = add_frac(frac1, frac2)
print(frac1, "+", frac2, "=", add_res)

# call sub_frac
sub_res = sub_frac(frac1, frac2)
print(frac1, "+", frac2, "=", sub_res)

# call reduce_frac
red = reduce_frac(frac3)
print("frac3 original:", frac3, "\nfrac3 simplified:", red)

# end main
