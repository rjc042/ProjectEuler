
def read_tris(f_string):
    triangles = []
    with open(f_string) as f:
        tri_lines = f.readlines()
        for tri in tri_lines:
            tri = tri.split(",")
            tri = [[int(tri[i]), int(tri[i + 1])] for i in range(0, len(tri), 2)]
            triangles.append(tri)
    return triangles


def check_tri(triangle):
    x_coors = [coor[0] for coor in triangle]
    y_coors = [coor[1] for coor in triangle]

    slopes = [float(y_coors[i]) / float(x_coors[i]) for i in range(len(triangle) - 1)]

    x2, y2 = x_coors[len(triangle) - 1], y_coors[len(triangle) - 1]
    check_list = [(y_coors[i] - slopes[1-i] * x_coors[i]) * (y2 - slopes[1-i] * x2) for i in range(len(slopes))]

    return all(d < 0 for d in check_list)


def main():
    f_string = "p102_triangles.txt"
    triangles = read_tris(f_string)

    ans = sum([check_tri(tri) for tri in triangles])
    print ("ANSWER: %d" % ans)



main()
