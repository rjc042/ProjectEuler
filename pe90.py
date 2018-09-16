import itertools

# 10 choose 6
# Make sure to include digits not on die 1 in die 2

def works(N, NUM_SIDES, side_a, side_b):
    # free_sides = side_b[2*NUM_SIDES - N::]
    for i in range(1, N):
        s = str(i*i)
        if i < 4:
            s = '0' + s
        # if (s[0] in free_sides) or (s[1] in free_sides):
        #     continue
        if (s[0] in side_a and s[1] not in side_b) and (s[1] in side_a and s[0] not in side_b):
            return False
        elif (s[0] in side_b and s[1] not in side_a) and (s[1] in side_b and s[0] not in side_a):
            return False
    return True

# def get_sides_a(N, NUM_SIDES):
#     '''
#     Return list of distinct side A arrangements
#     '''
#     sides_a_tuples = itertools.combinations(range(N), NUM_SIDES)
#     sides_a = []
#     for side_a in sides_a_tuples:
#         side_a = list(side_a)
#         if (6 in side_a) or (9 in side_a):
#             side_a += [6,9]
#             side_a = list(set(side_a))
#         sides_a.append(side_a)
#
#     sides_a = set(tuple(side_a) for side_a in sides_a)
#     return [list(side_a) for side_a in sides_a]

def get_side_eff(side):
    if 6 in side or 9 in side:
        return list(set(side + [6,9]))
    else:
        return side

def get_sides_a(N, NUM_SIDES):
    '''
    Return list of distinct side A arrangements
    '''
    sides_a = itertools.combinations(range(N), NUM_SIDES)
    return [list(side_a) for side_a in sides_a]


def get_free_sides(NUM_SIDES, pool, nums_needed):
    num_choose = NUM_SIDES - len(nums_needed)
    # if (6 in nums_needed) or (9 in nums_needed):
    #     num_choose += 1
    free_sides_tuples = itertools.combinations(pool, num_choose)

    # free_sides = []
    # for free_side in free_sides_tuples:
    #     free_side = list(free_side)
    #     if (6 in free_side) or (9 in free_side):
    #         free_side += [6,9]
    #         free_side = list(set(free_side))
    #     free_sides.append(free_side)
    #
    # free_sides = set(tuple(free_side) for free_side in free_sides)
    free_sides = [list(free_side) for free_side in free_sides_tuples]
    return free_sides

def get_nums_needed(N, side_a):
    '''
    Get list of elements not in side_a
    '''
    side_a_eff = get_side_eff(side_a)

    nums_needed_all = [i for i in range(N) if i not in side_a_eff]
    if 6 in nums_needed_all or 9 in nums_needed_all:
        nums_needed_6 = [i for i in nums_needed_all if i != 6]
        nums_needed_9 = [i for i in nums_needed_all if i != 9]
        return [nums_needed_6, nums_needed_9]
    else:
        return [nums_needed_all]

def get_side_pairs(N, NUM_SIDES):
    '''
    Return 2d list of pairs of sides to check
    '''
    # nums_str = "".join(range(N))
    side_pairs = []

    # sides_a = itertools.combinations(range(N), NUM_SIDES)
    sides_a = get_sides_a(N, NUM_SIDES)
    for side_a in sides_a:
        nums_needed_2d = get_nums_needed(N, side_a)
        print "Side A: ", side_a

        for nums_needed in nums_needed_2d:
            print "Numbers needed: ", nums_needed
            pool = [i for i in range(N) if i not in nums_needed]
            free_sides = get_free_sides(NUM_SIDES, pool, nums_needed)

            for free_side in free_sides:
                print "Free side: ", free_side
                side_b = nums_needed + list(free_side)
                side_pairs.append([side_a, side_b])
                print "Side A: ", side_a, " Side B: ", side_b
                print "Effective A: ", get_side_eff(side_a), " Effective B: ", get_side_eff(side_b), "\n"
    return side_pairs

def main():
    N = 10
    NUM_SIDES = 6

    side_pairs = get_side_pairs(N, NUM_SIDES)
    side_pairs = []
    for side_pair in old_side_pairs:
        if side_pair not in side_pairs and side_pair[::-1] not in side_pairs:
            side_pairs.append(side_pair)

    count = 0
    for side_pair in side_pairs:
        # print side_pair
        side_a = get_side_eff(side_pair[0])
        side_b = get_side_eff(side_pair[1])
        side_a = "".join([str(i) for i in side_a])
        side_b = "".join([str(i) for i in side_b])
        # print "A: %s , B: %s --> %d" % (side_a, side_b, works(N, NUM_SIDES, side_a, side_b))
        if works(N, NUM_SIDES, side_a, side_b):
            count += 1
    print "ANSWER: %d" % (count)




main()
