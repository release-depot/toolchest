#!/usr/bin/env python
import os


def generate_gitreview(path, project, host, port,
                       branch, remote, rebase=1):
    """Write a new .gitreview file to disk.

        :param str path: Directory where the file will be written
        :param str project: Name of the project
        :param str host: Gerrit host
        :param str port: Port for Gerrit host
        :param str branch: Git branch to use as defaultbranch
        :param str remote: Git remote to use as defaultremote
        :param int rebase: if 0, then the defaultrebase will be 0
                                 and the changes won't be rebased by default
                           if 1, then the defaultrebase will be 1
                                 and the changes will be rebased by default
    """
    with open(os.path.join(path, '.gitreview'), 'w') as fp:
        fp.write('[gerrit]\n')
        fp.write(f'host={host}\n')
        fp.write(f'port={port}\n')
        fp.write(f'project={project}.git\n')
        fp.write(f'defaultbranch={branch}\n')
        fp.write(f'defaultremote={remote}\n')
        fp.write(f'defaultrebase={rebase}\n')
