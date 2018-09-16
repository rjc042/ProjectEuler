import numpy as np

# Check rows / cols for one 0
# Check boxes for one 0
# For 1 box
    # For each elt not in box, check if in 2 vertical AND 2 hor boxes


# Try 1
# If 1 in box, row, or col
    # Try 2
# Else go to next 0


def read_grids(filename):
    N = 9
    with open(filename) as f:
        grids = f.readlines()

    grids = [list(grids[i])[:N] for i in range(len(grids)) if i % 10 != 0]
    grids = list(map(lambda grid: [int(x) for x in grid], grids))
    grids = [grids[i: i + N] for i in range(len(grids)) if i % 9 == 0]
    return grids

def print_grid(grid):
    for line in grid:
        print line
    print ""

def in_box(grid, i, j, n):
    box_i = 3 * (i // 3)
    box_j = 3 * (j // 3)
    box = np.array(grid)[box_i: box_i + 3, box_j: box_j + 3]
    return list(box.flatten()).count(n) > 1

def check_n(grid, i, j, n):
    grid[i][j] = n
    grid_col_j = [grid[l][j] for l in range(9)]
    # print i,j
    # print "grid: ", grid
    # print ""
    # print "column: ", grid_col_j
    if grid[i].count(n) > 1 or grid_col_j.count(n) > 1:
        return False
    elif in_box(grid, i, j, n):
        return False
    else:
        return True


def get_elt(grid, i, j):
    for test_n in range(1, 10):
        # print "Checking n = ", test_n
        if check_n(grid, i, j, test_n):
            # print "n = ", test_n, " works!"
            return test_n
    return 0


def backtrack(grid, zero_coors, zc_i= -2):
    prev_i, prev_j = zero_coors[zc_i][0], zero_coors[zc_i][1]
    # print "\nPrevious zero was at: ", prev_i, prev_j, " and set to: ", grid[prev_i][prev_j]
    # grid[prev_i][prev_j] = (grid[prev_i][prev_j] + 1) % 9
    # grid[prev_i][prev_j] = (grid[prev_i][prev_j] + 1) % 9

    test_n0 = grid[prev_i][prev_j]
    for test_n in range(test_n0 + 1, 10):
        # print "Checking: ", test_n
        # print "Now we have ", grid[prev_i][prev_j], " at ", prev_i, prev_j
        if check_n(grid, prev_i, prev_j, test_n):
            # print "After backtracking, we set ", test_n, " at ", prev_i, prev_j
            # print '-'*50 + "\n\n"
            grid[prev_i][prev_j] = test_n
            zc_i += 1

            return [grid, zc_i]

    grid[prev_i][prev_j] = 0
    # print "\nGoing back again..."
    zc_i -= 1
    return backtrack(grid, zero_coors, zc_i)

def update_zeros_after_backtrack(grid, zero_coors, zc_i):
    # print "Now we go to the next zero: ", zero_coors[zc_i][0], zero_coors[zc_i][1]
    i, j = zero_coors[zc_i][0], zero_coors[zc_i][1]
    grid_ij = get_elt(grid, i, j)
    # print "New entry for this zero is: ", grid_ij

    while grid_ij and zc_i < 0:

        grid[i][j] = grid_ij
        # print "Now we go AGAIN to the next zero: ", i,j
        # print "New entry is: ", grid[i][j]
        zc_i += 1
        i, j = zero_coors[zc_i][0], zero_coors[zc_i][1]

        grid_ij = get_elt(grid, i, j)

    if not grid_ij:
        # print "\nBacktracking within update function!"

        backtrack_res = backtrack(grid, zero_coors, zc_i)
        grid_to_be_updated = backtrack_res[0]
        zc_i = backtrack_res[1]
        grid = update_zeros_after_backtrack(grid_to_be_updated, zero_coors, zc_i)

    return grid



def get_next_zero(grid, i, j):
    while grid[i][j] != 0:
        j = (j + 1) % 9
        i += (9 - j) // 9
        if i > 8:
            break
    return (i,j)

def solve(grid):
    i, j = 0, 0
    zero_coors = []
    while i < 9:
        next_zero = get_next_zero(grid, i, j)
        i, j = next_zero[0], next_zero[1]
        if i == 9:
            break
        zero_coors += [next_zero]
        # print "\nZero at: ", next_zero
        # print "Zeros: ", zero_coors

        grid[i][j] = get_elt(grid, i, j)

        if not grid[i][j]:
            # print "\nBacktracking!"

            backtrack_res = backtrack(grid, zero_coors)
            grid_to_be_updated = backtrack_res[0]
            zc_i = backtrack_res[1]
            grid = update_zeros_after_backtrack(grid_to_be_updated, zero_coors, zc_i)

        # grid[i][j] = get_elt(grid, i, j)

        # print "Zero has been set to: ", grid[i][j]

        # if not grid[i][j]:
        #     print "\nBacktracking!"
        #     zc_i = -2
        #     grid = backtrack(grid, zero_coors, zc_i)

        # print "    ", [grid[zc[0]][zc[1]] for zc in zero_coors]
        #
        # print "=" * 50 + "\n\n"
        # print "\nGRID: \n"
        # print_grid(grid)
    return grid

def main():
    filename = "p096_sudoku.txt"
    grids = read_grids(filename)
    print solve(grids[0])
    # solved_grids = [solve(grid) for grid in grids]
    # three_digits_list = [s_grid[0][:3] for s_grid in solved_grids]
    # three_digits_list = list(map(lambda tri: [str(d) for d in tri], three_digits_list))
    # ans = sum(list(map(lambda tri: int("".join(tri)), three_digits_list)))
    # print "ANSWER: %d" % ans
    # print "Testing: \n"
    # print_grid(grid)







main()
