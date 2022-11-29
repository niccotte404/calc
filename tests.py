import unittest
from main import Calc, ReadingFile

class Test(unittest.TestCase):


    def test_calc(self):
        self.assertEqual(Calc("3425 + 25"), 3450)
        self.assertEqual(Calc("20 * 400"), 8000)
        self.assertEqual(Calc("300 - 9"), 291)
        self.assertEqual(Calc("99 - 199"), -100)
        self.assertEqual(Calc("2**3"), 8)
        self.assertEqual(Calc("20 / 5"), 4)


if __name__ == "__main__":
    unittest.main()
