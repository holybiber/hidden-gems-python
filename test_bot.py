
import unittest

from bot import entfernung


class ElisaBotCase(unittest.TestCase):
    def test_entfernung(self):
        self.assertEqual(entfernung(10, 10, 19, 3), 16)
        self.assertEqual(entfernung(8, 17, 2, 8), 15)
        self.assertEqual(entfernung(3, 9, 5, 7), 4)
        self.assertEqual(entfernung(16, 3, 16, 11), 8)
        self.assertEqual(entfernung(38, 7, 1, 7), 37)
        self.assertEqual(entfernung(25, 38, 25, 38), 0)


if __name__ == '__main__':
    unittest.main()
