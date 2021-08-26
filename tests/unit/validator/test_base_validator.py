import pytest

from toolchest.validator.base import BaseValidator
from toolchest.validator.simple import validate_string


def misbehaving_validator(item_to_validate):
    return "I didn't read the docs!"


def test_returns_true_with_good_validator():
    result = BaseValidator.validate(validate_string, 'my string')
    assert result is True


def test_throws_value_error_on_bad_input():
    with pytest.raises(ValueError, match='5 is not a string'):
        BaseValidator.validate(validate_string, 5)


def test_noncompliant_validator():
    with pytest.raises(ValueError, match='5 failed validation'):
        BaseValidator.validate(misbehaving_validator, 5)
