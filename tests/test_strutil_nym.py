#!/usr/bin/env python

""" Tests for the nym function from strutil module """

from toolchest.strutil import nym


def test_identity():
    assert nym('abc') == 'abc'


def test_spaces():
    assert nym('abc def') == 'abc_def'


def test_tabs():
    assert nym('abc\tdef') == 'abc_def'


def test_lowercase():
    assert nym('aBcDeF') == 'abcdef'
