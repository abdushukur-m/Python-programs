import unittest
from juftSon import juftSon_ajrat

sonlar = [1, 2, 45, 12, 79, 20, 21, 11, 7]

class Test_juftSon(unittest.TestCase):
    def test_son(self):
        natija = juftSon_ajrat(sonlar)
        for son in natija:
            self.assertTrue(son%2==0)

unittest.main()

