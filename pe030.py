
def get_sum_dig_pow(n, pow):
    sum_dig_pow = 0
    while n:
        sum_dig_pow += (n % 10) ** pow
        n //= 10
    return sum_dig_pow

def get_good_nums_sum(max_n, pow):
    total = 0
    for n in range(max_n):
        if n == get_sum_dig_pow(n, pow):
            # print n
            total += n
    return total - 1

def main():
    MAX_N = 1000000
    POW = 5

    total = get_good_nums_sum(MAX_N, POW)
    print ("ANSWER: %d") % (total)




main()
