
def is_pandigital_9(nums_list, n):
    nums_list_str = [str(num) for num in nums_list]
    str_num = "".join(nums_list_str)
    if len(str_num) != n:
        return False

    str_num_set = set(str_num)
    if len(str_num_set) < n:
        return False

    check_list = [str(i) for i in range(1, n+1)]
    return str_num_set == set(check_list)

def check_tens(tens, target_n):
    prod_list = []

    a_start = 10 ** tens
    a_end = a_start * 10

    num_digits_rem = target_n - tens - 1

    b_start = 10 ** (num_digits_rem // 2 - 1)
    max_prod = 10 * a_start * b_start

    for a in range(a_start+1, a_end):
        b_end = max_prod / a + 1

        for b in range(b_start, b_end):
            check_list = [a,b,a*b]
            if is_pandigital(check_list, target_n):
                prod_list += [a*b]

    return prod_list

def get_prods(target_n):
    tens_pow_min, tens_pow_max = 0, 3

    prod_list = []
    for pow in range(tens_pow_min, tens_pow_max):
        prod_list += check_tens(pow, target_n)

    return prod_list




def main():
    TARGET_N = 9


    prod_list = get_prods(TARGET_N)
    prod_set = set(prod_list)
    sum_prods = sum(prod_set)

    print ("ANSWER: %d") % (sum_prods)


main()
