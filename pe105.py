import itertools

def read_sets(file_name):
    sets_file = open(file_name)
    sets = sets_file.readlines()
    sets_file.close()

    for i in range(len(sets)):
        set_i = sets[i]
        set_i = set_i.split(",")
        set_i[-1] = set_i[-1][:-1]
        set_i = [int(n) for n in set_i]
        sets[i] = set_i

    return sets

def check_i(B, C):
    return S(B) != S(C)

# def check_ii(B, C):
#     return not (len(C) > len(B) and S(C) < S(B))


def check_ii(A):
    A_lh = sorted(A)
    A_hl = A_lh[::-1]

    if len(A) % 2 == 0:
        max_i = len(A) / 2 - 1
    else:
        max_i = len(A) / 2

    for i in range(max_i):
        B = A_lh[:i+2]
        C = A_hl[:i+1]
        if sum(B) > sum(C):
            continue
        else:
            return False
    return True


def check(subsets):
    for subset in subsets:
        B, C = subset[0], subset[1]
        # print B, C
        # if check_i(B,C) and check_ii(B,C):
        if check_i(B,C):
            continue
        else:
            return False
    return True


def get_subsets(A):
    subsets = []
    for i in range(1, len(A) / 2 + 1):
        combos_len_i = list(itertools.combinations(A, i))
        combos_len_i = [list(c) for c in combos_len_i]
        for B in combos_len_i:
            C_pool = [a for a in A if a not in B]
            for j in range(len(C_pool)):
                Cs = list(itertools.combinations(C_pool, i))
                Cs = [list(c) for c in Cs]
                for C in Cs:
                    # print [B,C]
                    subsets.append([B,C])
    return subsets



def S(A):
    ''' Sum of elements of set A of size n '''
    return sum(A)

def is_special_sum(A):
    if check_ii(A):
        A_subsets = get_subsets(A)
        is_special = check(A_subsets)
        # print is_special
        return is_special
    else:
        return False

def get_sum_of_special_sums(set_list):
    special_As = list(filter(is_special_sum, set_list))
    # print "Special As: ", special_As
    return sum([S(A) for A in special_As])

def main():
    FILE_NAME = "pe105.txt"
    set_list = read_sets(FILE_NAME)
    # A = [[157, 150, 164, 119, 79, 159, 161, 139, 158]]
    # set_list = A
    sum_of_special_sums = get_sum_of_special_sums(set_list)
    print "ANSWER: ", sum_of_special_sums


main()
