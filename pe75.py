

def is_exactly_1(L, MAX_L):
    num_tris = 0
    a = 1
    b = L / 2 - a
    c = L - (a + b)
    while a < L / 3:
        while b < c:
            # if L == 120:
            #     print a,b,c
            if a**2 + b**2 == c**2:
                num_tris += 1
                if num_tris > 1:
                    return False
                # print "L = %d" % (L)
                # print "GOOD: ", a, b, c
            b += 1
            c = L - a - b
        a += 1
        b = max([L / 2 - a, a])
        c = L - (a + b)
    return num_tris


def main():
    MAX_L = 1000

    num_exactly_1 = 0
    for L in range(10, int(MAX_L)):
        num_exactly_1 += is_exactly_1(L, MAX_L)
    print num_exactly_1


main()
