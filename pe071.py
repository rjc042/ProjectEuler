
def get_closest(max_d, target_num, target_den):
    n = 1
    for d in range(2, max_d):
        while target_den * n < target_num * d:
            n += 1
    return n - 1



def main():
    TARGET_NUM, TARGET_DEN = 3, 7
    MAX_D = 1000000

    left_num = get_closest(MAX_D, TARGET_NUM, TARGET_DEN)
    print ("ANSWER: %d" % left_num)

main()
