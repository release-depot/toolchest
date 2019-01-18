"""
Test introspection methods
"""

import pytest  # NOQA
from toolchest.introspect import build_repr, build_attrs, check_if_property


class SomeClass(object):

    def __init__(self, key1=None):
        self._key1 = key1

    @property
    def key1(self):
        return self._key1


@pytest.fixture()
def an_object():
    return SomeClass()


class TestCheckIfProperty(object):

    def test_true_if_property(self, an_object):
        assert check_if_property(an_object, 'key1') is True

    def test_false_if_not_property(self, an_object):
        SomeClass.not_a_key = 'some value'
        assert check_if_property(an_object, 'not_a_key') is False


class TestBuildAttrs(object):

    def test_no_attrs(self, an_object):
        attrs_dict = build_attrs(an_object)
        assert an_object.key1 is None
        assert attrs_dict.get('key1') is None

    def test_returns_key_value_list(self):
        obj = SomeClass(key1="farkle")
        attrs_dict = build_attrs(obj)
        assert obj.key1 == 'farkle'
        assert attrs_dict.get('key1') == 'farkle'


class TestBuildRepr(object):

    def test_returns_string(self):
        obj = SomeClass(key1="farkle")
        obj_str = build_repr(obj)
        expected = "SomeClass({'key1': 'farkle'})"
        assert obj_str == expected
