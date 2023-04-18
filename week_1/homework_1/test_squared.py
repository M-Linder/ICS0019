import unittest
from square_matlin.nums_squared import numbers_added_and_squared


class PackageTests(unittest.TestCase):

    def test_invalid_inputs(self):
        # Floating point integers.
        self.assertRaises(TypeError, numbers_added_and_squared, 0.1, 0.2)
        # Strings.
        self.assertRaises(TypeError, numbers_added_and_squared, 'a', 'b')

    def test_simple_inputs(self):
        # Two Squared.
        self.assertEqual(numbers_added_and_squared(1, 1), 4, "Should be 4.")
        # Three Squared.
        self.assertEqual(numbers_added_and_squared(1, 2), 9, "Should be 9.")
        # Four Squared.
        self.assertEqual(numbers_added_and_squared(1, 3), 16, "Should be 16.")
        # Five Squared.
        self.assertEqual(numbers_added_and_squared(2, 3), 25, "Should be 25.")
        # Six Squared.
        self.assertEqual(numbers_added_and_squared(3, 3), 36, "Should be 36.")
        # Seven Squared.
        self.assertEqual(numbers_added_and_squared(3, 4), 49, "Should be 49.")
        # Eight Squared.
        self.assertEqual(numbers_added_and_squared(3, 5), 64, "Should be 64.")
        # Nine Squared.
        self.assertEqual(numbers_added_and_squared(3, 6), 81, "Should be 81.")
        # Ten Squared.
        self.assertEqual(numbers_added_and_squared(3, 7), 100, "Should be 100.")

    def test_harder_inputs(self):
        # 281 Squared.
        self.assertEqual(numbers_added_and_squared(280, 1), 78961, "Should be 78 961.")
        # 486 Squared.
        self.assertEqual(numbers_added_and_squared(485, 1), 236196, "Should be 23 6196.")
        # 884 Squared.
        self.assertEqual(numbers_added_and_squared(883, 1), 781456, "Should be 781 456.")
