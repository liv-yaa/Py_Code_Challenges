import unittest
from pybitesJan2020 import JSONParser

class TestMethods(unittest.TestCase):
    j = JSONParser()
    # print(j, dir(j))
    

    def test_j_created(self):
        """ Tests if j was created """
        print('self.j created OK', self.j, dir(self.j))

        assert bool(self.j) == True


    def test_most_prolific_automaker_1999(self):
        # print('test 1999', self.j.most_prolific_automaker(1999))
        assert self.j.most_prolific_automaker(1999) == 'Dodge'


    def test_most_prolific_automaker_2008(self):
        assert self.j.most_prolific_automaker(2008) == 'Toyota'


    def test_most_prolific_automaker_2013(self):
        assert self.j.most_prolific_automaker(2013) == 'Hyundai'


    def test_get_models_volkswagen(self):
        models = self.j.get_models('Volkswagen', 2008)
        print(len(models))
        # sets are unordered
        assert len(models) == 2
        assert 'Jetta' in models
        assert 'Rabbit' in models


    def test_get_models_nissan(self):
        print(len(self.j.get_models('Nissan', 2000)))

        assert self.j.get_models('Nissan', 2000) == {'Pathfinder'}


    def test_get_models_open(self):
        # not in data set
        assert self.j.get_models('Opel', 2008) == set()


    def test_get_models_mercedes(self):
        models = self.j.get_models('Mercedes-Benz', 2007)
        assert len(models) == 3
        assert 'SL-Class' in models
        assert 'GL-Class' in models
        assert 'CL-Class' in models




if __name__ == '__main__':
    unittest.main()