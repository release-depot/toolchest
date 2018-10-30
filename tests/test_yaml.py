#!/usr/bin/env python

""" Tests for the yaml module """

import os.path

from toolchest.yaml import parse


def test_simple_string():
    expected = {'a': 1}
    input_str = '---\na: 1'
    actual = parse(input_str)
    assert actual == expected


def test_bad_string():
    expected = {}
    input_str = ':'
    actual = parse(input_str)
    assert actual == expected


def test_file_read(datadir):
    file_to_load = os.path.join(datadir, 'sample.yml')
    expected = {'a': 1,
                'b': 2,
                'c': [7, 8, 9]}
    file_handle = open(file_to_load, 'r')
    actual = parse(file_handle.read())
    assert actual == expected
