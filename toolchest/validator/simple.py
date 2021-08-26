def validate_string(str_to_validate):
    """
    Validates that the value passed in is a string.

    :param str str_to_validate: A value to validate
    :return: Returns True if pattern matches
    :raises ValueError: If the passed in item is not a string, a ValueError
            is thrown.
    """

    if type(str_to_validate) is not str:
        raise ValueError(f"{str_to_validate} is not a string")
    return True
