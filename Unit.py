import unittest
from For_unit import recursia


class MyTestCase(unittest.TestCase):
    def test_recursia(self):
        side_square = recursia(1, 2, 0)
        self.assertEqual(side_square, None)


if __name__ == '__main__':
    unittest.main()
