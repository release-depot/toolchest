#! /usr/bin/env python
"""Interface to get a configured logger"""

import importlib


def getLogger(config=None):
    """
    Returns a logger object of the type specified.

    :param config: Dictionary of values to configure the desired logger object.

    For example, to use the default python logger, you can
    either simply pass None, or specify any details supported by
    the toolchest default driver for the python logger.  You
    would specify the default logger (with custom loglevel) with:
    ::

      {'driver':'toolchest.logging.drivers.default',
      'root':{'level':DEBUG}}

    The toolchest logging wrapper code specifies a toplevel element in the
    config dict of 'driver', pointing at the driver that will load the
    desired configuration and return a logger to use.

    Each driver must implement getLogger, so we can invoke it the same way from
    this interface. In theory, drivers could be released as separate modules.

    """
    if not config:
        config = _default_config()
    try:
        module = importlib.import_module(config.get('driver'))
        return module.getLogger(config)
    except ModuleNotFoundError as e:
        logger = getLogger(_default_config())
        logger.error('Loading the default driver, {0}'.format(e.msg))
        return logger


def _default_config():
    return {'driver': 'toolchest.logging.drivers.default'}
