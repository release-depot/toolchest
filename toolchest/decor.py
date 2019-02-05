#!/usr/bin/env python

import os
import itertools
import sys
import time
import signal

display_color = True
_done = True

HILIGHT = '[1m'
NORMAL = '[0m'

COLORS = {'red': '\033[31m',
          'yellow': '\033[33m',
          'blue': '\033[34m',
          'green': '\033[32m',
          'default': '\033[0m'}


def ask_yesno(message):
    ret = input(message + ' [y/N]? ')
    if ret in ('y', 'Y', 'yes', 'YES'):
        return True
    return False


def color_string(string, color):
    if display_color is not True:
        return string

    ret_string = ''
    if color in COLORS:
        ret_string = '{0}{1}{2}'.format(COLORS[color],
                                        string,
                                        COLORS['default'])
    else:
        ret_string = string

    return ret_string


def usleep(msec):
    time.sleep(msec / 1000000.0)


def exithandler(sig, frame):
    global _done
    _done = True


class Spinner(object):

    def __init__(self, startmsg='', endmsg=''):
        global _done

        self._endmsg = endmsg
        sys.stdout.write(startmsg)
        sys.stdout.flush()

        # No-op when redirecting
        if not sys.stdout.isatty():
            self._pid = -1
            return

        self._pid = os.fork()
        if self._pid:
            return
        signal.signal(signal.SIGTERM, exithandler)
        _done = False
        self._spinner = itertools.cycle('-/|\\')
        sys.stdout.write('\\')
        while not _done:
            sys.stdout.write('\b' + next(self._spinner))
            sys.stdout.flush()
            usleep(100000)
        sys.stdout.write('\b')
        sys.stdout.flush()
        exit(0)

    def __del__(self):
        if self._pid > 0:
            os.kill(self._pid, signal.SIGTERM)
            os.wait()
        if self._pid != 0:
            sys.stdout.write(self._endmsg)
            sys.stdout.flush()

    def __enter__(self):
        pass

    def __exit__(self, t, v, traceback):
        if t is not None:
            raise


# Object wrapper around python-prettytable. Fakes it
# if prettytable is not installed.
class PrettyTable(object):
    def __init__(self, column_names):
        self.ugly = True
        self.cols = column_names
        self.rows = []
        self.align = None

        try:
            import prettytable
            self.pt = prettytable.PrettyTable(column_names)
            self.ugly = False
            return
        except ImportError:
            pass

    def add_row(self, row):
        if not self.ugly:
            return self.pt.add_row(row)

        if len(row) != len(self.cols):
            msg = 'Row length is {0}, but should be {1}'
            raise ValueError(msg.format(str(len(row)), str(len(self.cols))))
        self.rows.append(row)

    def get_string(self):
        if not self.ugly:
            try:
                if self.align is not None:
                    self.pt.align = self.align
            except AttributeError as e:
                print(e)
                pass
            return self.pt.get_string()

        s = ''
        s = s + '\t'.join([str(q) for q in self.cols]) + '\n'
        for r in self.rows:
            s = s + '\t'.join([str(q) for q in r]) + '\n'
        return s


def box(msg):
    print('+-' + ('-' * len(msg)) + '-+')
    print('| ' + msg + ' |')
    print('+-' + ('-' * len(msg)) + '-+')


def line(msg):
    return '-' * len(msg)
