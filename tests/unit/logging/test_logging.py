"""Test logging functionality"""

import logging
from unittest.mock import MagicMock
from toolchest.logging import logger


def test_gets_default_logger():
    """
    GIVEN we request a logger with the default toolchest logger
    WHEN we specify the root log level
    THEN we get back a default python logger, with that level set.
    """
    mylogger = logger.getLogger({'driver': 'toolchest.logging.drivers.default',
                                'root': {'level': 'DEBUG'}})
    assert isinstance(mylogger, logging.Logger)
    assert mylogger.getEffectiveLevel() == logging.DEBUG


def test_no_logger_specified():
    """
    GIVEN we request a logger without specifying any details
    THEN we get back a default python logger with log level = WARNING
    """
    mylogger = logger.getLogger()
    assert isinstance(mylogger, logging.Logger)
    assert mylogger.getEffectiveLevel() == logging.WARNING


def test_driver_not_found():
    """
    GIVEN we request a logger with a driver that cannot be found
    THEN we get back a default python logger with log level = WARNING
    """
    logging.Logger.error = MagicMock()
    mylogger = logger.getLogger({'driver': 'foo.bar.baz'})

    mylogger.error.assert_called_with(
        "Loading the default driver, No module named 'foo'")
    assert isinstance(mylogger, logging.Logger)
    assert mylogger.getEffectiveLevel() == logging.WARNING
