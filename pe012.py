
def count_divs(tri_num):
    check_divs = range(1, int(tri_num ** 0.5) + 1)
    half_divisors = list(filter(lambda i: tri_num % i == 0, check_divs))
    num_divs = 2 * len(half_divisors)

    tri_num_sqrt = tri_num ** 0.5
    if int(tri_num_sqrt) == tri_num_sqrt:
        num_divs -= 1
    return num_divs


def get_first_tri_num(target):
    tri_num = 0
    num_divs = 0
    increment = 1
    while num_divs <= target:
        tri_num += increment
        increment += 1
        num_divs = count_divs(tri_num)
    return tri_num

def main():
    TARGET_NUM_DIVS = 500
    first_tri_num = get_first_tri_num(TARGET_NUM_DIVS)
    print ("ANSWER: %d" % first_tri_num)

main()
