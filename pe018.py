
def read_tri(tri_file):
    tri_f = open(tri_file)
    tri_lines = tri_f.readlines()
    tri_f.close()

    tri_lines = [line.split(" ") for line in tri_lines]
    tri_lines = [[int(num[:2]) for num in line] for line in tri_lines]

    return tri_lines

def get_bin_paths(triangle):
    num_rows = len(triangle)
    num_paths = int('1' * (num_rows - 1), 2) + 1

    bin_paths = []
    for p in range(num_paths):
        bin_str = bin(p)[2:]
        bin_path = '0' * (num_rows - len(bin_str)) + bin_str
        bin_paths.append(bin_path)

    return bin_paths

def get_path_total(path, triangle):
    path = [int(b) for b in path]
    idx = 0
    path_total = 0
    for row in range(len(path)):
        idx += path[row]
        path_total += triangle[row][idx]
    return path_total


def get_max_path(bin_paths, triangle):
    max_path = 0
    for path in bin_paths:
        path_total =  get_path_total(path, triangle)
        if path_total > max_path:
            max_path = path_total
    return max_path



def main():
    tri_file = 'PE-Text-Files/pe018.txt'
    triangle = read_tri(tri_file)
    bin_paths = get_bin_paths(triangle)
    max_path = get_max_path(bin_paths, triangle)
    print ("ANSWER: %d") % max_path

main()
