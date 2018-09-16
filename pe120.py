

def remainder(a, n):
    r = ((a-1)**n + (a+1)**n) % a**2
    return r

def get_sequence(a):
    rem_list = []
    n = 1
    while True:
        r = remainder(a, n)
        rem_list.append(r)

        if (n % 2 == 0) and (rem_list[:len(rem_list) / 2] == rem_list[len(rem_list) / 2:]):
            return rem_list[:len(rem_list) / 2]

        n += 1

def get_rmax(a):
    seq = get_sequence(a)
    return max(seq)

def main():
    a_min, a_max = 3, 1000
    n = 25
    ans = sum([get_rmax(a) for a in range(a_min, a_max+1)])
    print "ANSWER: %d" % ans



main()
