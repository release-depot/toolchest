#!/usr/bin/env python

""" Tests for the yaml module """

import os.path
import subprocess

import pytest

from toolchest.yaml import parse, write


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


def test_bad_write():
    data = {'a': 'apple', 'b': 'banana'}
    output_file = '/bad/path/data.yml'
    with pytest.raises(FileNotFoundError):
        write(output_file, data)
    assert not os.path.exists(output_file)


def test_good_write(tmp_path):
    expected = {'a': 'apple', 'b': 'banana'}
    output_file = os.path.join(tmp_path, 'generated.yml')
    write(output_file, expected)
    with open(output_file, 'r') as check_fn:
        parsed = parse(check_fn.read())
        assert parsed == expected


def test_read_write_roundtrip(datadir, tmp_path):
    output_file = os.path.join(tmp_path, 'generated.yml')
    input_file = os.path.join(datadir, 'sample.yml')
    with open(input_file, 'r') as input_fh:
        output_data = parse(input_fh.read())
        write(output_file, output_data)
        # If an exception is raised the files contain a diff and the test
        # will fail. We want to make sure we can write out in the same format
        # that we read in.
        subprocess.check_call(['diff', input_file, output_file])
