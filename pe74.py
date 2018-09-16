import math as math

def sum_factorial_digits(n):
    digits_list = [int(c) for c in str(n)]
    return sum([math.factorial(i) for i in digits_list])

def get_chain_len(n):
    chain = [n]
    next_term = sum_factorial_digits(n)
    while next_term not in chain:
        chain.append(next_term)
        next_term = sum_factorial_digits(next_term)
    return len(chain)

def count_chains(TARGET_LEN, START, END):
    count = 0
    good_perms, bad_perms = [], []
    for n in range(START, END):
        sorted_digits_list = sorted(list(str(n)))
        if sorted_digits_list in good_perms:
            count += 1
        elif sorted_digits_list in bad_perms:
            continue
        elif get_chain_len(n) == TARGET_LEN:
            good_perms.append(sorted_digits_list)
            count += 1
        else:
            bad_perms.append(sorted_digits_list)
    return count

def main():
    START, END = 1, int(1e6)
    TARGET_LEN = 60
    ans = count_chains(TARGET_LEN, START, END)
    print "ANSWER: %d" % ans

main()
