from decimal import *
import math

def digital_sum(n, num_digits):
    getcontext().prec = num_digits + 10
    sqrt_n = Decimal(n).sqrt()
    decimals_list = list(str(sqrt_n))
    decimals_list.remove('.')
    decimals_list = [int(d) for d in decimals_list]
    decimals_list = decimals_list[:num_digits]
    return sum(decimals_list)

def get_sum_digital_sums(max_n, num_digits):
    sum_digital_sums = 0
    for n in range(2, max_n):
        sqrt_n = n ** 0.5
        if sqrt_n != int(sqrt_n):
            sum_digital_sums += digital_sum(n, num_digits)
    return sum_digital_sums


def main():
    NUM_DIGITS = 100
    MAX_N = 100
    
    sum_digital_sums = get_sum_digital_sums(MAX_N, NUM_DIGITS)
    print ("ANSWER: %d" % sum_digital_sums)

main()
