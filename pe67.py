
def read_tri(f):
    tri_file = open(f, 'r')
    tri_list = tri_file.readlines()
    for i in range(len(tri_list)):
        tri_list[i] = tri_list[i].split(" ")
        tri_list[i] = map(int, tri_list[i])
    tri_file.close()
    tri_list = tri_list[::-1]
    return tri_list

def collapse(rows):
    for i in range(len(rows)-1):
        # print "rows[i] = ", rows[i]
        for j in range(len(rows[i]) - 1):
            left_sum = rows[i][j] + rows[i+1][j]
            right_sum = rows[i][j+1] + rows[i+1][j]
            max_sum = max(left_sum, right_sum)
            rows[i+1][j] = max_sum
    return rows[-1][0]



def main():
    f = 'p067_triangle.txt'
    rows = read_tri(f)
    return collapse(rows)

ans = main()
print "ANSWER: " + str(ans)
