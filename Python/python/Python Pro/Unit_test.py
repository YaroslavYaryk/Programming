import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6)

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6,)

    def test_geter(self):
        aaa = "hello world"
        self.assertAlmostEqual(len(aaa), 11)

    def factorial(self, x):
        sstorage = 1
        for i  in range(2, x+1):
            sstorage *=i
        return sstorage        

    def test_factorial(self):
        self.assertEqual(self.factorial(5), 120)


if __name__ == '__main__':
    unittest.main()