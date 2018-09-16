
def count_mults(N):
    total = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def main():
    N = 1000
    total = count_mults(N)
    print "ANSWER: ", total

main()
