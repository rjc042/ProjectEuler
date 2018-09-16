
def primesList(n):
    lst = [2]
    i = 3
    while i < n:
        div = 2
        while div < int(i**0.5 + 2):
            if i%div == 0:
                break
            elif div == int(i**0.5 + 1):
                lst.append(i)
            div += 1
        i += 1
    return lst


def checkOddComp(n):
    if i%2 == 0:
        return False
    elif i not in primes_list:
        return True

def findPair(n):
    i = 0
    while primes_list[i] <= n:
        j = 1
        check = primes_list[i] + 2*j**2
        while check <= n:
            check = primes_list[i] + 2*j**2
            if check == n:
                return [primes_list[i], j]
            j += 1
        i += 1
    return False

primes_list = primesList(1e5)
# print primes_list

i = 2
while i < int(1e4):
    if checkOddComp(i):
        if findPair(i) == False:
            print "Answer: ", i
            break
    i += 1
