"""
Test the utility methods
"""

import pytest  # NOQA
from toolchest.rpm.rpmvercmp import labelCompare, rpmvercmp


class TestRpmvercmp(object):

    def test_equal(self):
        assert rpmvercmp('1.2', '1.2') == 0
        assert rpmvercmp('a', 'a') == 0

    def test_basic(self):
        assert rpmvercmp('1.1', '1.2') == -1
        assert rpmvercmp('1.2', '1.1') == 1
        assert rpmvercmp('1.2a', '1.2') == 1
        assert rpmvercmp('1.2', '1.2a') == -1
        assert rpmvercmp('1.2', '1.1abcde') == 1
        assert rpmvercmp('1', '11') == -1
        assert rpmvercmp('11', '1') == 1
        assert rpmvercmp('a', 'b') == -1
        assert rpmvercmp('b', 'a') == 1

    def test_lead_zeroes(self):
        assert rpmvercmp('1.2.2031', '1.2.02031') == 0
        assert rpmvercmp('01.02.0000002031', '1.2.2031') == 0
        assert rpmvercmp('1.2.2031', '1.2.00002030') == 1
        assert rpmvercmp('1.2.2030', '1.2.00002031') == -1

    def test_excessive_version_length(self):
        assert(rpmvercmp('9999999999999999999999999999999999999999999',
                         '9999999999999999999999999999999999999999999') == 0)
        assert(rpmvercmp('9999999999999999999999999999999999999999999',
                         '9999999999999999999999999999999999999999998') == 1)
        assert(rpmvercmp('9999999999999999999999999999999999999999998',
                         '9999999999999999999999999999999999999999999') == -1)

    def test_weird_versions(self):
        a = 'a'
        b = '1'
        assert rpmvercmp(a, b) == -1
        assert rpmvercmp(b, a) == 1

        a = '1.01.001'
        b = '1.1.1'
        assert rpmvercmp(a, b) == 0

        a = '~1'
        assert rpmvercmp(a, b) == -1
        assert rpmvercmp(b, a) == 1

        a = '1~1'
        assert rpmvercmp(a, b) == -1
        assert rpmvercmp(b, a) == 1

        a = '----'
        b = '-'
        assert rpmvercmp(a, b) == 0

        a = '1-'
        b = '1'
        assert rpmvercmp(a, b) == 0

        a = '1-'
        b = '-'
        assert rpmvercmp(a, b) == 1
        assert rpmvercmp(b, a) == -1

    def test_bad_types(self):
        with pytest.raises(ValueError):
            rpmvercmp({}, '1.0')
        with pytest.raises(ValueError):
            rpmvercmp('1.0', {})


class TestLabelCompare(object):

    def test_basic(self):
        a = ('0', '6.0.0', '2.el7ost')
        b = ('0', '6.0.1', '2.el7ost')
        assert labelCompare(a, b) == -1
        assert labelCompare(a, a) == 0
        assert labelCompare(b, a) == 1
        assert labelCompare(b, b) == 0

    def test_vr_only(self):
        # no epoch => epoch = 0
        a = ('6.0.0', '2.el7ost')
        b = ('6.0.1', '2.el7ost')
        assert labelCompare(a, b) == -1
        assert labelCompare(a, a) == 0
        assert labelCompare(b, a) == 1
        assert labelCompare(b, b) == 0

    def test_zero_epoch(self):
        # 0 and no epoch are the same
        a = ('0', '6.0.0', '2.el7ost')
        b = ('6.0.1', '2.el7ost')
        assert labelCompare(a, b) == -1
        assert labelCompare(a, a) == 0
        assert labelCompare(b, a) == 1
        assert labelCompare(b, b) == 0

        # librpm seems to set '' to 0
        a = ('', '1.0', '1')
        b = ('1.0', '1')
        c = (0, '1.0', '1')
        d = ('0', '1.0', '1')
        assert labelCompare(a, b) == 0
        assert labelCompare(a, c) == 0
        assert labelCompare(a, d) == 0
        assert labelCompare(b, c) == 0
        assert labelCompare(b, d) == 0
        assert labelCompare(c, d) == 0

    def test_eq_epoch(self):
        a = ('1', '6.0.0', '2.el7ost')
        b = ('1', '6.0.1', '2.el7ost')
        assert labelCompare(a, b) == -1
        assert labelCompare(a, a) == 0
        assert labelCompare(b, a) == 1
        assert labelCompare(b, b) == 0

    def test_neq_epoch(self):
        # a always wins.
        a = ('1', '6.0.0', '2.el7ost')
        b = ('0', '6.0.1', '2.el7ost')
        assert labelCompare(a, b) == 1
        assert labelCompare(a, a) == 0
        assert labelCompare(b, a) == -1
        assert labelCompare(b, b) == 0

    def test_bad_types(self):
        a = '1:6.0.0-2.el7ost'
        b = 1
        with pytest.raises(ValueError):
            labelCompare(a, b)
        with pytest.raises(ValueError):
            labelCompare(b, a)

    def test_bad_length(self):
        a = ('1', '6.0.0', '2.el7ost', 1)
        b = ('0', '6.0.1', '2.el7ost')
        with pytest.raises(ValueError):
            labelCompare(a, b)
        with pytest.raises(ValueError):
            labelCompare(b, a)

    def test_bad_epoch(self):
        a = ('abcde', '1.0', '1')
        b = ('1.0', '1')
        with pytest.raises(ValueError):
            labelCompare(a, b)

    def test_weird_versions(self):
        a = ('0', 'a', '1')
        b = ('0', '1', '1')
        assert labelCompare(a, b) == -1
        assert labelCompare(b, a) == 1

        a = ('0', '1.01.001', '1')
        b = ('0', '1.1.1', '1')
        assert labelCompare(a, b) == 0

        a = ('0', '~1', '1')
        b = ('0', '1', '1')
        assert labelCompare(a, b) == -1
        assert labelCompare(b, a) == 1

        a = ('0', '1~1', '1')
        b = ('0', '1', '1')
        assert labelCompare(a, b) == -1
        assert labelCompare(b, a) == 1
