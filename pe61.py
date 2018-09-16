import numpy as np

def is_triangle(num):
    twice_num = 2 * num
    n = int(twice_num ** 0.5)
    return n * (n + 1) == twice_num

def is_square(num):
    n = num ** 0.5
    return n == int(n)

def is_pentagonal(num):
    n = (1 + (1 + 24 * num) ** 0.5) / 6.0
    return n == int(n)

def is_hexagonal(num):
    n = 0.25 * (1 + (1 + 8 * num) ** 0.5)
    return n == int(n)

def is_heptagonal(num):
    n = 0.1 * (3 + (9 + 40 * num) ** 0.5)
    return n == int(n)

def is_octagonal(num):
    n = (2 + (4 + 12 * num) ** 0.5) / 6.0
    return n == int(n)



# def is_cyclic(lst):
#     middle = 2
#     lst_strings = [str(x) for x in lst]
#     halves = [[int(c[:middle]), int(c[middle:])] for c in lst_strings]
#     print halves
#     former_digits = [num_pair[0] for num_pair in halves]
#     latter_digits = [num_pair[1] for num_pair in halves]
#
#     distinct_halves = list(np.array(halves).flatten())
#     num_distinct_halves = len(set(distinct_halves))
#
#     if num_distinct_halves == len(lst):
#         chain = [halves[0]]
#         find_half = halves[0][1]
#         for half_i in range(len(halves)):
#             print "Chain: ", chain
#             try:
#                 idx = former_digits.index(find_half)
#                 next_num_pair = halves[idx]
#                 chain.append(next_num_pair)
#                 find_half = next_num_pair[1]
#             except ValueError:
#                 return False
#         return True
#
#     return False



def which_poly_type(check_list, n):
    return list(map(lambda f: f(n), check_list))


def contains_all_poly_nums(check_list, lst):
    set_of_poly_types = np.matrix([which_poly_type(check_list, n) for n in lst], dtype = int)
    return np.linalg.det(set_of_poly_types) != 0

def split_into_cycle(n, num_digits, cycle_length):
    middle = num_digits / 2
    n = str(n) + str(n)[:middle]
    cycle_strings = [n[middle * i: middle * i + num_digits] for i in range(cycle_length)]
    cycle_ints = [int(c) for c in cycle_strings]
    cycle_strings = [str(c) for c in cycle_ints]
    num_digits_in_terms = [len(c) - num_digits for c in cycle_strings]
    if not np.any(num_digits_in_terms):
        return cycle_ints
    else:
        return False

def get_cycle(check_list, num_digits, cycle_length):
    num_distinct_digits = cycle_length * num_digits / 2
    start, end = 10 ** (num_distinct_digits - 1), 10 ** num_distinct_digits
    for cyc in range(start, end):
        print cyc
        if cyc % 10000000000 == 0:
            print cyc
        check_cycle = split_into_cycle(cyc, num_digits, cycle_length)
        if check_cycle and contains_all_poly_nums(check_list, check_cycle):
            return check_cycle
    return False

def main():
    CYCLE_LENGTH = 6
    NUM_DIGITS = 4

    check_list = [is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal]

    cycle = get_cycle(check_list, NUM_DIGITS, CYCLE_LENGTH)
    print ("ANSWER: %d" % sum(cycle))




main()
