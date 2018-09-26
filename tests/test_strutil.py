import unittest

from toolchest.strutil import list_or_splitstr


class test_list_or_splitstr(unittest.TestCase):

    def test_identity(self):
        self.assertEqual(list_or_splitstr([1, 2]), [1, 2])

    def test_oops(self):
        with self.assertRaises(ValueError):
            list_or_splitstr({})
        with self.assertRaises(ValueError):
            list_or_splitstr(1)
        with self.assertRaises(ValueError):
            list_or_splitstr(None)

    def test_normal(self):
        self.assertEqual(list_or_splitstr('a b c'), ['a', 'b', 'c'])
        self.assertEqual(list_or_splitstr('a,b c'), ['a', 'b', 'c'])
        self.assertEqual(list_or_splitstr('a, b, c'), ['a', 'b', 'c'])
        self.assertEqual(list_or_splitstr('''a
    b        c'''), ['a', 'b', 'c'])
        self.assertEqual(list_or_splitstr('a	b	c'), ['a', 'b', 'c'])
