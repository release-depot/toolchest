#!/usr/bin/env python

import re


def list_or_splitstr(arg):
    if type(arg) is list:
        return arg
    if type(arg) is not str:
        raise ValueError('arg is not a string or list')

    return [x for x in re.split('[\t\n, ]', arg) if x != '']


def split_file(arg):
    with open(arg, 'r') as f:
        text = f.read()
        return list_or_splitstr(text)
    return None


def regex_chars(arg):
    s = set('[]()|.*+')
    if any((c in s) for c in arg):
        return True
    return False


def regex_match(pattern, arg):
    if re.match(pattern, arg) is not None:
        return True
    return False
