import itertools

def getPandigitals(s):
    pans = list(itertools.permutations(s))
    pans = [list(p) for p in pans if p[0] != '0']
    for i in range(len(pans)):
        pans[i] = int(''.join(pans[i]))
    return pans

def checkTriads(p):
    p = str(p)
    i = 1
    triads = []

    bool = True
    factors = [2,3,5,7,11,13,17]
    j = 0
    while i < 8:
        triad = int(p[i] + p[i+1] + p[i+2])
        if triad%factors[j] != 0:
            bool = False
            break
        i += 1
        j += 1
    return bool


def main():
    pandigitals = getPandigitals('0123456789')

    total = 0
    for p in pandigitals:
        if checkTriads(p):
            total += p
    print "ANSWER: ", total

main()
