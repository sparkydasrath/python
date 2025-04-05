import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    # def test_fibonacci_zero(self):
    #     self.assertEqual(fibonacci(0), "Input should be a positive integer")

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    # def test_fibonacci_negative(self):
    #     with self.assertRaises("Input should be a positive integer"):
    #         fibonacci(-1)

if __name__ == '__main__':
    unittest.main()