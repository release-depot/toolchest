#! /usr/bin/env python
"""Implementation of a driver that uses the standard python logger."""

import logging
import logging.config


def getLogger(config):
    """
    Returns a python stdlib logger

    :param config:  Dictionary of values meeting the criteria in the
                    `Configuration dictionary schema
                    <https://docs.python.org/3.7/library/logging.config.html#logging-config-dictschema>`_.

    """
    if 'version' not in config:
        config['version'] = 1
    if len(config) > 2:
        logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.setLevel(config.get('root', {}).get('level', logging.WARNING))
    return logger
