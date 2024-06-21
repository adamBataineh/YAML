import unittest
from yourCodeFileName import function1, function2

class TestYourCodeFile(unittest.TestCase):
    
    def test_function1(self):
        self.assertEqual(function1(1), 0)
        self.assertNotEqual(function1(5), 0)
        self.assertTrue(function1(2) == 1)
        self.assertFalse(function1(2) == 3)
    
    def test_function2(self):
        self.assertEqual(function2(2, 1), 3)
        self.assertEqual(function2(2.1, 1.2), 3.3)
        self.assertAlmostEqual(function2(0.1, 0.2), 0.3)
        self.assertNotAlmostEqual(function2(2, 2), 3)

if __name__ == '__main__':
    unittest.main()
