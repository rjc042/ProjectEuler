import numpy as np

def read_grid(grid_filename):
    grid_file = open(grid_filename)
    grid_lines = grid_file.readlines()
    grid_file.close()

    grid = []
    for grid_line in grid_lines:
        grid_line = grid_line.split(" ")
        grid_line = [int(n) for n in grid_line]
        grid.append(np.array(grid_line))
    return np.array(grid)

def flip_matrix(grid):
    flipped = []
    for row in grid:
        flipped.append(row[::-1])
    return np.array(flipped)


def get_max_row(grid, num_elts):
    max_prod = 0
    for row in grid:
        row_products = [np.prod(row[n: n + num_elts]) for n in range(len(row) - num_elts)]
        max_prod_in_row = max(row_products)
        if max_prod_in_row > max_prod:
            max_prod = max_prod_in_row
    return max_prod

def get_max_diag(grid, num_elts):
    max_prod = 0
    for row_i in range(len(grid) - num_elts):
        row_products = []
        for col_j in range(len(grid) - num_elts):
            prod = np.prod([grid[row_i + k][col_j + k] for k in range(num_elts)])
            row_products.append(prod)
        max_prod_in_row = max(row_products)
        if max_prod_in_row > max_prod:
            max_prod = max_prod_in_row
    return max_prod


def get_max_prod(grid, num_elts):
    grid_transpose = np.transpose(grid)
    grid_flipped = flip_matrix(grid)

    max_horizontal = get_max_row(grid, num_elts)
    max_vertical = get_max_row(grid_transpose, num_elts)
    max_diag_1 = get_max_diag(grid, num_elts)
    max_diag_2 = get_max_diag(grid_flipped, num_elts)

    return max([max_horizontal, max_vertical, max_diag_1, max_diag_2])



def main():
    NUM_ELTS = 4
    grid_filename = 'p11_grid.txt'
    grid = read_grid(grid_filename)
    max_prod = get_max_prod(grid, NUM_ELTS)
    print ("ANSWER: %d"% max_prod)


main()
