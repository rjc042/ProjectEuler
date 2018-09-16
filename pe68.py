import itertools

def get_indices(num_sides):
    lst = []
    for i in range(num_sides, 2*num_sides):
        lst.append([i, i - num_sides, (i - num_sides + 1) % num_sides])
    return lst

def get_groups(perm, indices):
    groups = []
    for group_inds in indices:
        groups.append([perm[i] for i in group_inds])
        # groups.append(list(map(lambda i: perm[i], group_inds)))
    return groups

def check_totals(groups):
    group_totals = [sum(group) for group in groups]
    if len(set(group_totals)) == 1:
        return True
    else:
        return False

def get_groups_str_lst(groups):
    groups_str_lst = []
    for group in groups:
        s = [str(i) for i in group]
        groups_str_lst.append("".join(s))
    return groups_str_lst


def get_conc_str(groups_str_lst):
    int_list = [int(s) for s in groups_str_lst]
    ind = int_list.index(min(int_list))
    sorted_strings = [str(int_list[i % len(int_list)]) for i in range(ind, ind + len(int_list))]
    return "".join(sorted_strings)

def get_conc_int_lst(nodes, indices, target_str_len):
    conc_int_lst = []

    for perm in itertools.permutations(nodes):
        groups = get_groups(perm, indices)
        if check_totals(groups):
            groups_str_lst = get_groups_str_lst(groups)
            if len("".join(groups_str_lst)) == target_str_len:
                conc_string = get_conc_str(groups_str_lst)
                conc_int_lst.append(int(conc_string))
    return conc_int_lst


def main():
    num_sides = 5
    target_str_len = 16

    num_nodes = 2*num_sides
    nodes = [i for i in range(1, num_nodes+1)]
    indices = get_indices(num_sides)

    conc_int_lst = get_conc_int_lst(nodes, indices, target_str_len)
    ans = max(conc_int_lst)
    print "ANSWER: " + str(ans)


main()
