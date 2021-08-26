#!/usr/bin/env python
import hashlib

from toolchest.strutil import list_or_splitstr
from toolchest.validator.simple import validate_string
from toolchest.validator.base import BaseValidator


def generate_hash(list_to_hash, validator=validate_string):
    """
    Takes a list of strings in any order, sorts them for consistency, and
    generates a cryptographic hash to provide a unique representation of this
    combination of strings.

    :param list list_to_hash: List of Strings to turn into a hash
    :param func validator: A function to use to validate the format of items
                           in the list of Strings. This function should throw
                           a ValueError if the pattern does not match.
    :return: A String that is a hash of the passed in list.
    :raises ValueError: If the passed in list cannot be validated with the
                        passed in validator, a ValueError is thrown.
    """
    hash_obj = hashlib.sha3_512()
    list_to_hash = list_or_splitstr(list_to_hash)
    list_to_hash.sort()
    for item in list_to_hash:
        BaseValidator.validate(validator, item)
        hash_obj.update(bytes(item, 'utf-8'))
    return hash_obj.hexdigest()
