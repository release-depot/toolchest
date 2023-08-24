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


def nym(arg):
    '''
    This is for allowing case and quote flexibility for strings when
    searching dictionaries or other data sets based on user input (esp.
    from the command line) where the likelihood of key collisions is
    low. For example, if we want to search a dictionary, we'd check the
    nym of the value provided with the nym of the key to see if they
    match. This should not be used when likelihood of collisions is high.
    (Origin: Greek word meaning "name")

    Parameters:
        arg (string): A string to create the nym for

    Returns:
        ret (string): A lower-case string with whitespace swapped to _
    '''
    ret = arg.lower().replace(' ', '_')
    ret = ret.replace('\t', '_')
    return ret
