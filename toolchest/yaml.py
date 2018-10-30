#! /usr/bin/env python
""" Yaml related tools """

import yaml


def parse(yaml_data, logger=None):
    """
    Safely parse yaml data

    :param yaml_data: A string of yaml data to be parsed
    :param logger: Optional logger for potential errors
    :return: A dictionary formed out of the yaml data
    """
    ret_data = {}
    try:
        ret_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as exc:
        msg = 'Error in yaml data'
        if hasattr(exc, 'problem_mark'):
            error_str = 'Yaml Error at: (line: {0}, column: {1})'
            msg = error_str.format(exc.problem_mark.line + 1,
                                   exc.problem_mark.column + 1)
        if logger is not None:
            logger.error(msg)
        else:
            print(msg)
    return ret_data
