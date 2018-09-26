import unittest

from toolchest.rpm.rpmvercmp import rpmvercmp


class test_rpmvercmp(unittest.TestCase):

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
