
def get_num_rects(L,W):
    num_rects = 0
    for w in range(1, W+1):
        for l in range(1, L+1):
            num_across = L - l + 1
            num_down = W - w + 1
            num_rects += num_across * num_down
    return num_rects

def get_closest_area(target):
    min_diff = target

    for L in range(1, 1200):
        W = 1
        while W < L:
            num_rects = get_num_rects(L, W)
            if abs(num_rects - target) < min_diff:
                min_diff = abs(num_rects - target)
                area = L*W
            if num_rects > 2e6:
                break
            W += 1
    return area

def main():
    target = 2e6

    ans = get_closest_area(target)
    print "ANSWER: " + str(ans)



main()
