import unittest
from pybitesJan2020 import DateGenerator
from datetime import datetime
from itertools import islice
# from gendates import gen_special_pybites_dates

class TestMethods(unittest.TestCase):
    dg = DateGenerator()

    def test_gen_special_pybites_dates(self):
        print('self.dg', self.dg)

        gen = self.dg.gen_special_pybites_dates()
        dates = list(islice(gen, 10))

        print(dates)

        expected = [datetime(2017, 3, 29, 0, 0),
                    datetime(2017, 7, 7, 0, 0),
                    datetime(2017, 10, 15, 0, 0),
                    datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
                    datetime(2018, 1, 23, 0, 0),
                    datetime(2018, 5, 3, 0, 0),
                    datetime(2018, 8, 11, 0, 0),
                    datetime(2018, 11, 19, 0, 0),
                    datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
                    datetime(2019, 2, 27, 0, 0)]

        assert dates == expected

if __name__ == '__main__':
    unittest.main()