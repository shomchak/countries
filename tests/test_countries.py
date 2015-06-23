from countries import countries

from random import randint
from unittest import TestCase


class CountriesTest(TestCase):

    def get_map(self):
        dim_lower = 3
        dim_upper = 3

        n_colors = 2

        n_rows = randint(dim_lower, dim_upper)
        n_columns = randint(dim_lower, dim_upper)

        columns = []
        for r in range(n_rows):
            columns.append([randint(1, n_colors) for i in range(n_columns)])

        return columns

    def test_solve(self):
        m = self.get_map()
        n_countries = countries.solve(m)
        print n_countries
