# FailTest.py
import unittest

class TestAlwaysFail(unittest.TestCase):
    def test_false_is_true(self):
        self.assertTrue(False)  # Intentional Failure

if __name__ == '__main__':
    unittest.main()
