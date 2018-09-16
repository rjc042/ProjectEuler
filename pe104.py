#!/usr/bin/env python2.7


def check_last(F_n):
    if F_n < 100000000:
        return False
    else:
        last_nine_digits = F_n % int(1e9)
        return sorted(str(last_nine_digits)) == [str(i) for i in range(1,10)]

def check_first(F_n):
    if F_n < 100000000:
        return False
    else:
        first_nine_digits = str(F_n)[:9]
        # print first_nine_digits
        return sorted(first_nine_digits) == [str(i) for i in range(1,10)]


def get_k():
    a,b = 1,1
    n = 3
    while True:
        F_n = a + b
        a, b = b, F_n
        if check_last(F_n) and check_first(F_n):
            return n
        n += 1
    return False

def main():
    k = get_k()
    print ("ANSWER: %d") % (k)
    
main()
