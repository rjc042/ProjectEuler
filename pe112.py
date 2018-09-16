
def is_bouncy(n):
    n_list = [int(i) for i in list(str(n))]
    inc = all(n_list[i] <= n_list[i+1] for i in range(len(n_list) - 1))
    dec = all(n_list[i] >= n_list[i+1] for i in range(len(n_list) - 1))
    return not (inc or dec)

def min_target_prop(target):
    num_bouncy = 0
    n = 1
    prop = num_bouncy / float(n)
    while prop < target:
        n += 1
        num_bouncy += is_bouncy(n)
        prop = num_bouncy / float(n)
    return n

def main():
    TARGET_PROP = 0.99
    ans = min_target_prop(TARGET_PROP)
    print ("ANSWER: %d" % ans)

main()
