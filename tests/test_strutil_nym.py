#!/usr/bin/env python

""" Tests for the nym function from strutil module """

from toolchest.strutil import nym


def test_identity():
    assert nym('abc') == 'abc'
    assert nym('') == ''
    assert nym(None) is None


def test_spaces():
    assert nym('abc def') == 'abc_def'


def test_tabs():
    assert nym('abc\tdef') == 'abc_def'


def test_lowercase():
    assert nym('aBcDeF') == 'abcdef'


def test_underscores():
    assert nym('a.b') == 'a_b'
    assert nym('a-b+c') == 'a_b_c'


def test_removes():
    assert nym('a(b)[c]{d}/e=f') == 'abcdef'


def test_non_null():
    # If we pass in a string, we should get _something_ back,
    # even if all characters would otherwise be removed
    assert nym('()')


def test_integer():
    assert nym(1) == '1'


def test_params():
    assert nym('1', remove='1') == '_'
    assert nym('12', underscore='1') == '_2'
    assert nym('123', underscore='1', remove='3') == '_2'
