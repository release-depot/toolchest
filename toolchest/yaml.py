#! /usr/bin/env python
""" Yaml related tools """

import yaml


class IndentDumper(yaml.Dumper):
    """ Custom yaml dumper to ensure elements are indented """
    def increase_indent(self, flow=False, indentless=False):
        # We can't set indentless from the yaml.dump call to control behavior.
        # When this method is called, indentless is being set to True so it
        # can't be used in the call to super. We the super call to always be
        # False.
        return super().increase_indent(flow=flow, indentless=False)


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


def write(filename, yaml_data, sort_keys=False):
    """
    Write out yaml data to a file

    :param filename: The name of the file to write the data
    :param yaml_data: A string of yaml data to be parsed
    :param sort_keys: Have the yaml data's keys sorted on write
    :return: None
    """

    # open the file for write, if it does not exist create it.
    with open(filename, 'w') as output_file:
        # write yaml header
        output_file.write('---\n\n')
        # write the actual data
        yaml.dump(yaml_data, output_file, Dumper=IndentDumper,
                  default_flow_style=False, sort_keys=sort_keys)
