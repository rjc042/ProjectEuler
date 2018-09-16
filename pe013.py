

def read_grid(grid_file):
    grid_f = open(grid_file)
    grid_str = grid_f.readlines()
    grid_f.close()

    grid_int = [int(num) for num in grid_str]
    return grid_int

def get_ten_digits(grid, num_digits):
    sum_grid = sum(grid)
    sum_grid_str = str(sum_grid)
    return sum_grid_str[:num_digits]

def main():
    NUM_DIGITS = 10
    grid_file = "PE-Text-Files/pe013.txt"
    grid = read_grid(grid_file)
    digits = get_ten_digits(grid, NUM_DIGITS)
    print "ANSWER: ", digits

main()
