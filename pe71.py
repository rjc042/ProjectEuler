from fractions import gcd

def get_fracs(MAX_D):
    lst_3d = []
    for d in range(2, MAX_D + 1):                   # Loop through denominators
        for n in range(1, d):                       # Loop through numerators (< d)
            if n < 3.0*d/7 and gcd(n,d) == 1:
                lst_3d.append([[n,d],float(n)/d])
    # lst_3d = sorted(lst_3d, key = lambda x: x[1])
    return lst_3d

def get_left_float(lst_floats, target_float):
    min_diff = 1.0
    for frac in lst_floats:
        check = target_float - frac
        if check > 0 and check < min_diff:
            min_diff = check
            left_float = frac
    return left_float

def get_target_num(left_float, lst_floats, lst_str):
    ind = lst_floats.index(left_float)
    return lst_str[ind][0]


def main():
    MAX_D = int(1e6)
    target = [3,7]
    target_float = 3.0/7.0

    lst_3d = get_fracs(MAX_D)
    lst_str = [x[0] for x in lst_3d]
    lst_floats = [x[1] for x in lst_3d]

    left_float = get_left_float(lst_floats, target_float)

    ans = get_target_num(left_float, lst_floats, lst_str)
    print "ANSWER: " + str(ans)


main()
