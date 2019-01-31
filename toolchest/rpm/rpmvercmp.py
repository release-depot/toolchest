#!/usr/bin/env python

# (C) 2018 Red Hat, Inc.
# License: Same as librpm: GPL version 2, or at your option,
#          any later version.


# Python copy of rpmvercmp() from rpmvercmp.c
#
# This is _intentionally_ as verbose as possible in order to most
# closely match rpmvercmp.c from librpm.  It is *easy* to make this
# more "pythonic", but then it would be more difficult to track/
# update changes and keeping this implementation bug-for-bug
# compatible with rpmvercmp.c's implementation.
def rpmvercmp(left, right):
    """
    Determines which label string has a higher value.

    This is for purposes of determining with version of a build is newer, or if
    they are equivalent based on string comparison.

    :param left: The left value to compare. Must be a string.
    :param right: The right value to compare. Must be a string.
    :returns: -1, 0, or 1 if the left value is less than, equal to,
            or greater than, the right value, respectively
    """

    # Note: Enhancement, for Pungi
    if left == 'None':
        left = None
    if right == 'None':
        right = None
    if left is None and right is None:
        return 0
    if left is None and right is not None:
        return -1
    if left is not None and right is None:
        return 1
    # # End Enhancement # #

    if not isinstance(left, str):
        raise ValueError('left is not a string')
    if not isinstance(right, str):
        raise ValueError('right is not a string')

    if left == right:
        return 0

    llen = len(left)
    rlen = len(right)
    li = 0
    ri = 0
    isnum = False

    while li < llen or ri < rlen:
        while (li < llen) and (not left[li].isalnum()) and left[li] != '~':
            li = li + 1
        while (ri < rlen) and (not right[ri].isalnum()) and right[ri] != '~':
            ri = ri + 1

        # The C code will compare vs. \0 here in some cases, which we can't
        # do directly, so watch for running past the end of the string and
        # assign a non-tilde if needed for this block. We need two try blocks
        # since we need to check these values independently.
        left_str = ''
        right_str = ''
        try:
            left_str = left[li]
        except IndexError:
            pass
        try:
            right_str = right[ri]
        except IndexError:
            pass

        if (left_str == '~' or right_str == '~'):
            if (left_str != '~'):
                return 1
            if (right_str != '~'):
                return -1
            li = li + 1
            ri = ri + 1
            continue

        if (li >= llen or ri >= rlen):
            break

        lp = li
        rp = ri

        if (left[lp].isdigit()):
            while (lp < llen and left[lp].isdigit()):
                lp = lp + 1
            while (rp < rlen and right[rp].isdigit()):
                rp = rp + 1
            isnum = True
        else:
            while (lp < llen and left[lp].isalpha()):
                lp = lp + 1
            while (rp < rlen and right[rp].isalpha()):
                rp = rp + 1
            isnum = False

        str1 = left[li:lp]
        str2 = right[ri:rp]

        if len(str1) == 0:
            return -1
        if len(str2) == 0:
            if isnum:
                return 1
            else:
                return -1

        if isnum:
            # Clear leading zeroes, if any
            str1 = str(int(str1))
            str2 = str(int(str2))

            if len(str1) > len(str2):
                return 1
            if len(str2) > len(str1):
                return -1

        if str1 != str2:
            if str1 < str2:
                return -1
            else:
                return 1

        li = lp
        ri = rp

    if li >= llen and ri >= rlen:
        return 0

    if li >= llen:
        return -1
    return 1


# Python implementation of rpm.labelCompare that does not need
# the RPM C libraries/packages; logic is from rpmvercmp.c
# rpmVersionCompare() function.
def labelCompare(left, right):
    """
    Determines which label tuple has a higher value.

    This is for purposes of determining with version of a build is newer, or if
    they are equivalent taking into account epoch, version, release.

    :param left: The left value to compare. Must be a tuple of (epoch, version,
                 release) or (version, release).
    :param right: The right value to compare. Must be a tuple of (epoch,
                  version, release) or (version, release).
    :returns: -1, 0, or 1 if the left value is less than, equal to,
              or greater than, the right value, respectively.
    """

    if not isinstance(left, tuple):
        raise ValueError('left is not a tuple')
    if not isinstance(right, tuple):
        raise ValueError('right is not a tuple')

    epoch_l = 0
    epoch_r = 0
    if len(left) == 3:
        if left[0] != '':
            epoch_l = int(left[0])
        version_l = str(left[1])
        release_l = str(left[2])
    elif len(left) == 2:
        version_l = str(left[0])
        release_l = str(left[1])
    else:
        raise ValueError('left is not a tuple of 2 or 3')

    if len(right) == 3:
        if right[0] != '':
            epoch_r = int(right[0])
        version_r = str(right[1])
        release_r = str(right[2])
    elif len(right) == 2:
        version_r = str(right[0])
        release_r = str(right[1])
    else:
        raise ValueError('right is not a tuple of 2 or 3')

    if epoch_l < epoch_r:
        return -1
    if epoch_l > epoch_r:
        return 1

    rc = rpmvercmp(version_l, version_r)
    if rc != 0:
        return rc

    return rpmvercmp(release_l, release_r)
