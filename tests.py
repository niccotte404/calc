import unittest
from main import Calc, ReadingFile

class Test(unittest.TestCase):


    def test_calc(self):
<<<<<<< HEAD
        self.assertequal(Calc("3425 + 25"), 3450)
        self.assertequal(Calc("20 * 400"), 8000)
        self.assertequal(Calc("300 - 9"), 281)
        self.assertequal(Calc("99 - 199"), -100)
        self.assertequal(Calc("2**3"), 8)
        self.assertequal(Calc("20 / 5"), 4)
        
=======
        self.assertEqual(Calc("3425 + 25"), 3450)
        self.assertEqual(Calc("20 * 400"), 8000)
        self.assertEqual(Calc("300 - 9"), 291)
        self.assertEqual(Calc("99 - 199"), -100)
        self.assertEqual(Calc("2**3"), 8)
        self.assertEqual(Calc("20 / 5"), 4)

>>>>>>> 9afff774dedebf6fe125b91826d399a38d581627

if __name__ == "__main__":
    unittest.main()
