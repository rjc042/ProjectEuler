


def get_min_cube(target_num_occurences):
    num_occurences = 0
    sorted_cube_dict = {}
    n = 1
    while True:
        cube = n ** 3
        sorted_cube = sorted(str(cube))
        sorted_cube = "".join(sorted_cube)
        if sorted_cube in sorted_cube_dict:
            sorted_cube_dict[sorted_cube] += [cube]
            if len(sorted_cube_dict[sorted_cube]) == target_num_occurences:
                min_cube = sorted_cube_dict[sorted_cube][0]
                return min_cube
        else:
            sorted_cube_dict[sorted_cube] = [cube]

        n += 1




def main():
    TARGET_NUM_PERMS = 5

    min_cube = get_min_cube(TARGET_NUM_PERMS)
    print ("ANSWER: %d" % min_cube)




main()
