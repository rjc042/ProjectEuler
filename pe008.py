
def read_grid():
    f = open("pe8_grid.txt", 'r')
    grid = f.read()
    f.close()

    grid = "".join(grid.split())
    return [int(x) for x in grid]

def get_max(grid, CHECK_LENGTH):
    max_product = 0
    for i in range(len(grid) - CHECK_LENGTH):
        check = 1
        for j in range(CHECK_LENGTH):
            check *= int(grid[i+j])
        if check > max_product:
            max_product = check
    return max_product


def main():
    grid = read_grid()

    CHECK_LENGTH = 13
    ans = get_max(grid, CHECK_LENGTH)
    
    print "ANSWER: " + str(ans)


main()
