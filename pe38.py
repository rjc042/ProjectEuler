


def checkPan(i):
    goal = list(str(123456789))
    n = 1
    test_pand = ""
    while True:
        num = i*n
        test_pand += str(num)
        if sorted(test_pand) == goal:
            return int(test_pand)
            break
        elif len(test_pand) >= 9:
            return False
            break
        elif len(test_pand) < 9:
            n += 1


def main():
    pand_inputs = list(filter(checkPan, range(50000)))
    pandigitals = map(checkPan, pand_inputs)
    print "ANSWER:", max(pandigitals)

main()
