import numpy as np

def has_right_angle(m01, m02, m12):
    return bool(np.dot(m01, m02) * np.dot(m01, m12) * np.dot(m02, m12))

def get_pairs(L):
    coors = []
    for x1 in range(L+1):
        for y1 in range(1, L+1):
            for x2 in range(1, L+1):
                for y2 in range(L+1):
                    m01 = [y1, x1]
                    m02 = [y2, x2]
                    m12 = [y2 - y1, x2 - x1]
                    if m12 == [0,0]:
                        continue
                    elif not has_right_angle(m01, m02, m12):
                        flat_list = [c for pair in sorted([[x1,y1], [x2,y2]]) for c in pair]
                        coors.append(tuple(flat_list))

    return len(set(coors))



def main():
    L = 50

    ans = get_pairs(L)
    print "ANSWER: %d" % (ans)


main()
