import pytest

from toolchest.validator.simple import validate_string


def test_returns_true_for_string():
    result = validate_string('farkle')
    assert result is True


def test_raises_with_non_string():
    with pytest.raises(ValueError, match='5 is not a string'):
        validate_string(5)
    with pytest.raises(ValueError, match='None is not a string'):
        validate_string(None)
