class BaseValidator():

    @staticmethod
    def validate(validator, item_to_validate):
        """
        A method to allow calling of any validator, with checking to only
        return True or an error, so that the validator cannot inject code
        into the caller.

        :param func validator: A function to use to validate the format of an
                            item. This function should throw a ValueError if
                            the pattern does not match.
        :param obj item_to_validate: A value to validate
        :return: Returns True if pattern matches
        :raises ValueError: If the item cannot be validated with the
                            validator, a ValueError is thrown.
        """

        is_valid = validator(item_to_validate)
        if is_valid is True:
            return True
        else:
            # This should only happen if the validator tries to do something
            # besides returning True or ValueError.  The purpose is to
            # prevent malicious code being injected.
            msg = f"{item_to_validate} failed validation, "
            msg += f"{validator} does not implement correct interface"
            raise ValueError(msg)
