import unittest

from toolchest.genericargs import GenericArgs


class test_genericargs(unittest.TestCase):

    def setUp(self):
        self.data = GenericArgs({'one': '1', 'two': '2'})

    def test_basic(self):
        assert self.data == {'one': '1', 'two': '2'}

    def test_items(self):
        assert self.data.one == '1'
        assert self.data.two == '2'

    def test_attr_not_found(self):
        # Returns None
        assert self.data.whatever is None

    def test_key_not_found(self):
        with self.assertRaises(KeyError):
            self.data['whatever'] == 0
