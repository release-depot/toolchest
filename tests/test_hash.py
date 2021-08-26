import pytest

from toolchest.hash import generate_hash


def test_good_list():
    my_list = ['openstack-foo-13.0-1', 'openstack-foo-13.0-2']
    result = generate_hash(my_list)
    expected = 'e07350662d96f'
    assert expected in result


def test_different_order_lists_return_same_hash():
    my_list = ['openstack-foo-13.0-1', 'openstack-foo-13.0-2']
    my_list2 = ['openstack-foo-13.0-2', 'openstack-foo-13.0-1']
    result1 = generate_hash(my_list)
    result2 = generate_hash(my_list2)
    assert result1 == result2


def test_different_lists_return_different_hashes():
    my_list = ['openstack-foo-13.0-1', 'openstack-foo-13.0-2']
    my_list2 = ['foo-13.0-1', 'foo-13.0-2']
    result1 = generate_hash(my_list)
    result2 = generate_hash(my_list2)
    assert result1 != result2


def test_throws_value_error_on_bad_input():
    with pytest.raises(ValueError, match='arg is not a string'):
        generate_hash(5)
    with pytest.raises(ValueError, match='arg is not a string'):
        generate_hash(None)
    with pytest.raises(ValueError, match='5 is not a string'):
        generate_hash([5])
