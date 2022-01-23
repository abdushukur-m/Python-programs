import unittest
from capitalize_text import capitalize


text_txt1 = "is simply dummy text of the printing and typesetting industry."
text_txt2 ="has been the industrys standard dummy text ever since the 1500 s,"
texts = [text_txt1, text_txt2]

correct_txt1 = "Is Simply Dummy Text Of The Printing And Typesetting Industry."
correct_txt2 = "Has Been The Industrys Standard Dummy Text Ever Since The 1500 S,"
c_texts = [correct_txt1, correct_txt2]

class CapitalizeTest(unittest.TestCase):
    def testTxt(self):
        sample_txt = capitalize(texts)
        self.assertEqual(sample_txt, c_texts)

unittest.main()