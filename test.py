import unittest
from p import is_sq

class SqrtTestCase(unittest.TestCase):

    def test_if_four_has_sqrt(self):
        self.assertTrue(is_sq(4))

if __name__ == "__main__":
    unittest.main()
