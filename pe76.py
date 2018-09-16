
def find_elt(lst):
    # Find elt != 1 closest to end
    for i in range(len(lst)):
        if lst[::-1][i] != 1:
            return len(lst) - 1 - i
    return False

def get_sub_lst(lst, i):
    sub_target = sum(lst[i:])
    total = lst[i] - 1
    inc = lst[i] - 1
    sub_lst = [inc]
    while total < sub_target:
        if total + inc <= sub_target:
            total += inc
            sub_lst.append(inc)
        elif total + inc > sub_target:
            inc -= 1
    return sub_lst

def count_num_ways(n):
    num_ways = 1
    # print "total: ", n
    lst = [n-1, 1]
    while lst[0] != 1:
        # print "lst: ", lst
        ind = find_elt(lst)
        # print "Last elt != 1 is at: ", ind
        sub_lst = get_sub_lst(lst, ind)
        # print "Subbing in: ", sub_lst
        lst = lst[:ind] + sub_lst
        # print ""
        num_ways += 1
    return num_ways


def main():
    N = 100
    print count_num_ways(N)







main()
