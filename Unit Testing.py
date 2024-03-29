import unittest
import _compat_pickle
import calc
result = calc.add()

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)

        self.assertEqual(result, 15)
        #self.assertEqual(result, 14)
        #FAILED (failure=1)
        self.assertEqual(calc.add(10,5), 15)
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)
        self.assertEqual(calc.multiply(0,-10), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)


if __name__ == '__main__':
    unittest.main()