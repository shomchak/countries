
def solve(m):
    count = 0
    for i_c, column in enumerate(m):
        for i_r, val in enumerate(column):
            left = -1 if i_c == 0 else m[i_c - 1][i_r]
            upper = -1 if i_r == 0 else m[i_c][i_r - 1]
            upper_left = -1 if i_c == 0 or i_r == 0 else m[i_c - 1][i_r - 1]

            if left != val and upper != val:
                count += 1
            elif val == left and val == upper and val != upper_left:
                count -= 1
    return count
