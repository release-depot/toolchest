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


def nym(arg, underscore='+-. !?;:\'",\t', remove='()[]{}?<>/='):
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
        underscore (string): A set of characters to replace with underscores
        remove (string): A set of characters to remove from the return value

    Returns:
        ret (string): A lower-case string with characters translated
                      or removed.
    '''
    if (ret := arg) not in ('', None):
        tr = str.maketrans(underscore, '_' * len(underscore), remove)
        ret = str(arg).lower().translate(tr) or '_'

    return ret
