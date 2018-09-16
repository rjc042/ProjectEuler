import numpy as np

# L = 7
# mat = [[0,16,12,21,0,0,0], [16,0,0,17,20,0,0], [12,0,0,28,0,31,0],[21,17,28,0,18,19,23]]
# mat += [[0,20,0,18,0,0,11], [0,0,31,19,0,0,27], [0,0,0,23,11,27]]

# Start at A
# Choose least from A           (AC)
# Remove AC
# Choose least from A or C      (AB)
# Remove BA
# REMOVE (BC)
# Choose least from A, B, C     (BD)
# Remove DB
# Remove DA, DC
# Choose...                     (DE)
# Remove ED
# Remove EA, EB, EC

# Sub max in matrix + 1 for '-'


def read_mat(file_name):
    with open(file_name) as f:
        mat = f.readlines()
        mat = [line.split(",") for line in mat]

    # Cutoff new line characters
    L = len(mat)
    for line_i in range(L):
        last = mat[line_i][L-1]
        mat[line_i][L-1] = last[:len(last)-1]
    return mat

def get_max_total_weight(mat_str):
    max_weight, sum_int = 0, 0
    for line in mat_str:
        row_int = [int(c) for c in line if c != '-']
        max_row_weight = max(row_int)
        sum_int += sum(row_int)
        if max_row_weight > max_weight:
            max_weight = max_row_weight
    return [max_weight + 1, sum_int/2]

def convert_int_mat(mat, max_weight):
    for row_i in range(len(mat)):
        mat[row_i] = [max_weight if c == '-' else int(c) for c in mat[row_i]]
    return mat

def get_upper_tri(mat, max_weight):
    L = len(mat)
    upper_tri = [[max_weight] * row_i + mat[row_i][row_i:] for row_i in range(L)]
    upper_tri = np.array([np.array(row) for row in upper_tri])
    return upper_tri



def get_saving(mat, total_weight):
    min_weight = 0
    total_weight = 0
    for row_i in range(1, len(mat)):
        weights = [int(c) for c in mat[row_i] if c != '-']
        min_weight_in_row = min(weights)
        total_weight += sum(weights)
    return total_weight - min_weight



def main():
    file_name = "PE-Text-Files/p107_network.txt"
    original_mat = read_mat(file_name)
    num_nodes = len(original_mat)

    max_total_result = get_max_total_weight(original_mat)
    max_weight, total_weight = max_total_result[0] + 10, max_total_result[1]
    mat = convert_int_mat(original_mat, max_weight)

    print ("\nmax_weight = %d") % (max_weight)
    print ("total_weight = %d") % (total_weight)

    print "\nORIGINAL MATRIX"
    for line in original_mat:
        print line
    print ""

    print "\nNOW MATRIX:"
    for line in mat:
        print line
    print ""


    reduced_mat = max_weight * np.ones((num_nodes, num_nodes), dtype = int)
    print "\nInitializing reduced matrix:"
    for li in reduced_mat:
        print li
    print ""

    reduced_weight = 0
    row_i = 0
    row_i_list = [row_i]
    weights_pool = [mat[row_i] for row_i in row_i_list]
    for l in range(num_nodes - 1):
        print "\nRows (nodes) considered: \n", row_i_list

        # weights_pool_arr = np.array(weights_pool).flatten()
        weights_pool_arr = np.array(weights_pool)
        print "\nSelect min from weights_pool array: "
        print weights_pool_arr

        min_weight = weights_pool_arr.min()
        reduced_weight += min_weight
        print "\nMin in pool: ", min_weight
        min_ij = np.array(np.where(weights_pool == min_weight)).flatten()
        print "at min_ij: ", min_ij, " in weights_pool array"
        min_i, min_j = min_ij[0], min_ij[1]
        print "at ",  row_i_list[min_i], min_j, " in upper tri array"
        min_i = row_i_list[min_i]

        reduced_mat[min_i][min_j] = min_weight
        reduced_mat[min_j][min_i] = min_weight

        mat[min_i][min_j] = max_weight
        mat[min_j][min_i] = max_weight

        print "\nUPDATED REDUCED MATRIX:"
        for li in reduced_mat:
            print li
        print ""

        print "\nUPDATED ORIGINAL MATRIX:"
        for li in mat:
            print li
        print ""

        row_i_list += [min_j]
        weights_pool = [mat[row_i] for row_i in row_i_list]


        print "\nEND ITERATION\n"

    print ("Original total weight: %d") % (total_weight)
    print ("Reduced weight: %d") % (reduced_weight)
    saving = total_weight - reduced_weight
    print "ANSWER: %d" % saving

main()
# 259679
