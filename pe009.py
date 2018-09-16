from numpy import prod

def get_trio(target):
    a = 1
    while a < target:
        b = a
        while b < target:
            c = b
            while c < target:
                if a*a + b*b == c*c and a + b + c == target:
                    return [a,b,c]
                c += 1
            b += 1
        a += 1

def main():
    target = 1000
    trio = get_trio(target)
    ans = prod(trio)
    print "ANSWER: " + str(ans)


main()
