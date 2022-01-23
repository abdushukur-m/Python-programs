import unittest
from kattasi import eng_kichigi, eng_kattasi

class TestKattasi(unittest.TestCase):
    def test_katta(self):
        kattasi = eng_kattasi(100, 210, -45)
        self.assertEqual(kattasi, 210)

    def test_kichik(self):
        kichigi = eng_kichigi(100, 210, -45)
        self.assertEqual(kichigi, -45)

unittest.main() 