
def get_contact_pt(slope, x0, y0):
    x = x0 * slope ** 2 - y0 * slope
    x += 2 * (100.0 + (25.0 - x0 ** 2) * slope ** 2 + 2 * slope * x0 * y0 - y0 ** 2) ** 0.5
    x /= 4.0 + slope ** 2

    x2 = x0 * slope ** 2 - y0 * slope
    x2 -= 2 * (100.0 + (25.0 - x0 ** 2) * slope ** 2 + 2 * slope * x0 * y0 - y0 ** 2) ** 0.5
    x2 /= 4.0 + slope ** 2

    # print ("\nStarting from x0 = %f") % (x0)
    # print ("x = %f or x2 = %f") % (x,x2)
    # print ("|%f - %f| = %f\n |%f - %f| = %f") % (x,x0,abs(x-x0),x2,x0,abs(x2-x0))

    if abs(x2-x0) > abs(x-x0):
        x = x2
    # print ("x = %f\n") % (x)

    y = slope * (x - x0) + y0
    return [x, y]

def get_mirror_slope(x,y):
    return - 4.0 * x / y

def get_ref_slope(beam_slope, mirror_slope):
    return (2 * mirror_slope - beam_slope * (1 - mirror_slope ** 2)) / (1 - mirror_slope ** 2 + 2 * mirror_slope * beam_slope)

def count_contacts(x, y, x_width, beam_slope):
    num_contacts = 1
    while abs(x) > x_width or y < 0.0:
        mirror_slope = get_mirror_slope(x,y)
        beam_slope = get_ref_slope(beam_slope, mirror_slope)

        contact_pt = get_contact_pt(beam_slope, x,y)
        x, y = contact_pt[0], contact_pt[1]

        num_contacts += 1

    num_contacts -= 1
    return num_contacts


def main():
    x_width = 0.01
    x0, y0 = 0.0, 10.1
    x1, y1 = 1.4, -9.6
    beam_slope = (y1 - y0) / (x1 - x0)


    # contact_pt = get_contact_pt(beam_slope, x, y)
    # x, y = contact_pt[0], contact_pt[1]
    # print x,y

    num_contacts = count_contacts(x1, y1, x_width, beam_slope)
    print ("ANSWER: %d") % (num_contacts)




main()
