import sys
sys.path.append("C:\WorkSpace\python test")

import new


import unittest

class TestRemoveSpaces(unittest.TestCase):
    
    def test_spaces(self):
        strng = "   abc   "
        result = new.remove_spaces(strng)
        self.assertEqual(result, "ab")

if __name__ == '__main__':
    unittest.main()