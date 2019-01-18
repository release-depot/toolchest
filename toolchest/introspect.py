# -*- coding: utf-8 -*-
"""
Methods related to introspection of a class
"""


def check_if_property(instance, prop):
    """
    Check if a given value is a property on the specified class instance

    :param instance: An instance of some class
    :param prop: A value to check
    :return: True or False
    """
    return isinstance(getattr(instance.__class__, prop), property)


def build_attrs(instance):
    """
    Build a dict of attributes on a given instance

    :param instance: An instance of some class
    :return: Dict of all object attributes that are properties
    """
    return {prop: instance.__getattribute__(prop)
            for prop in dir(type(instance)) if
            check_if_property(instance, prop)}


def build_repr(instance):
    """
    Generic way to implement a __repr__ method for classes using properties

    :param instance: An instance of some class
    :return: String that can be eval'ed to an object
    """
    return f"{type(instance).__name__}({build_attrs(instance)})"
