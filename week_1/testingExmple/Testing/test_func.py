import unittest
from calculator import calculate as c


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(c(3, 4), 7)


if __name__ == '__main__':
    unittest.main()
