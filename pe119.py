
def make_dict():
    dict = {}
    for i in range(10):
        last_digits = [str(i ** j)[-1] for j in range(1, 10)]
        last_digits = list(set(last_digits))
        dict[str(i)] = last_digits
    return dict

def is_digit_power(n, digit_dict):
    sum_digits = sum([int(d) for d in str(n)])
    last_digit_sum = list(str(sum_digits))[-1]
    last_digit_n = list(str(n))[-1]

    if (sum_digits == 1) or (last_digit_n not in digit_dict[last_digit_sum]):
        return False

    while n % sum_digits == 0 and n > sum_digits:
        n = n / sum_digits
    return n == sum_digits

def get_a30(n, digit_dict, target):
    i = 1
    while i <= target:
        if is_digit_power(n, digit_dict):
            print n, i
            i += 1
        n += 1
    return n


def main():
    TARGET_LEN = 30
    MIN_N = 10
    DIGIT_DICT = make_dict()
    get_a30(MIN_N, DIGIT_DICT, TARGET_LEN)


main()
