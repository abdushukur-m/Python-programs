import unittest
from fibonacci import fibonachchi_qaytar

son = 21

class Test_fibonacci(unittest.TestCase):
    def test_true(self):
        self.assertTrue(fibonachchi_qaytar(son))


unittest.main()