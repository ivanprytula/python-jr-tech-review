def star_triangle(r):
    for x in range(r):
        print(' ' * (r - x - 1) + '*' * (2 * x + 1))  # *

        # print(' ' * (9 - 0 - 1) + '*' * (2 * 0 + 1))  #        *
        # print(' ' * (9 - 1 - 1) + '*' * (2 * 1 + 1))  #       ***
        # print(' ' * (9 - 2 - 1) + '*' * (2 * 2 + 1))  #      *****
        # print(' ' * (9 - 3 - 1) + '*' * (2 * 3 + 1))  #     *******
        # print(' ' * (9 - 4 - 1) + '*' * (2 * 4 + 1))  #    *********
        # print(' ' * (9 - 5 - 1) + '*' * (2 * 5 + 1))  #   ***********
        # print(' ' * (9 - 6 - 1) + '*' * (2 * 6 + 1))  #  *************
        # print(' ' * (9 - 7 - 1) + '*' * (2 * 7 + 1))  # ***************


star_triangle(9)
