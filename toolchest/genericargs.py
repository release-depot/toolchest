#!/usr/bin/env python


# For calling cmdline functions w/o using
# argparse
class GenericArgs(dict):
    def __getattr__(self, name):
        if (name in self):
            return dict.__getitem__(self, name)
        return None
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
