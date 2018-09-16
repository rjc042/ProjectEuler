from decimal import *

def reverse(d):
    frac_string = str(Decimal(1.0)/Decimal(d))
    return frac_string[-2::-1]

def get_cycle_length(d, reverse_string):
    n = 1
    while n < len(reverse_string):
        left_string = reverse_string[:n:]
        check_string = reverse_string[n:2*n:]
        if left_string == check_string:
            return len(left_string)
        n += 1


def main():
    getcontext().prec = 2000
    dict = {}
    for d in range(2,1000):
        max_length = 100
        if len(str(Decimal(1.0)/Decimal(d))) > max_length:
            reverse_string = reverse(d)
            cycle_length = get_cycle_length(d, reverse_string)
            dict[d] = cycle_length
    max_cycle_d = max(dict, key = dict.get)
    print ("ANSWER: %d" % max_cycle_d)

main()
