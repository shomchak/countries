
def solve(m):
    countries = [[0 for _ in col] for col in m]
    for i_c, column in enumerate(m):
        for i_r in range(len(column)):
            if _looks_new(i_c, i_r, m):
                _add_edge(i_c, i_r, countries)
            else:
                _adjust_edge(i_c, i_r, m, countries)
    return _count(countries)


def _looks_new(i_c, i_r, m):
    val = m[i_c][i_r]
    left = -1 if i_c == 0 else m[i_c][i_r]
    upper = -1 if i_r == 0 else m[i_c][i_r]

    return not (left == val or upper == val)


def _add_edge(i_c, i_r, countries):
    countries[i_c][i_r] = 1


def _adjust_edge(i_c, i_r, m, countries):
    val = m[i_c][i_r]
    i_upper = max(0, i_r - 1)
    i_left = max(0, i_c - 1)

    if m[i_c][i_upper] == val:
        countries[i_c][i_upper] = 0
    if m[i_left][i_r] == val:
        countries[i_left][i_r] = 0
    countries[i_c][i_r] = 1


def _count(countries):
    return sum(col.count(1) for col in countries)
